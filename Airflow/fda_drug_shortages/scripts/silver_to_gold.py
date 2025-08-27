"""Glue ETL script to transform silver to gold layer (dimensional model)."""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import *
import hashlib

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'export_date', 'silver_bucket', 'gold_bucket'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read silver layer data
silver_path = f"s3://{args['silver_bucket']}/processed/export_date={args['export_date']}/"
df = spark.read.parquet(silver_path)

# Create dimension tables
dim_drug = df.select(
    F.col("drug_name"),
    F.col("ndc"),
    F.col("related_treatments")
).distinct().withColumn(
    "drug_id", 
    F.md5(F.concat_ws("_", F.col("drug_name"), F.col("ndc")))
)

dim_manufacturer = df.select(
    F.col("manufacturer_name")
).distinct().withColumn(
    "manufacturer_id",
    F.md5(F.col("manufacturer_name"))
)

dim_status = spark.createDataFrame([
    ("Active", 1, True),
    ("Resolved", 2, False),
    ("Discontinued", 3, False),
    ("PartiallyResolved", 4, True)
], ["status_name", "status_id", "is_active"])

# Create fact table
fact_shortages = df.join(
    dim_drug.select("drug_name", "ndc", "drug_id"),
    on=["drug_name", "ndc"]
).join(
    dim_manufacturer.select("manufacturer_name", "manufacturer_id"),
    on="manufacturer_name"
).join(
    dim_status.select("status_name", "status_id"),
    df.status == dim_status.status_name
).select(
    F.col("shortage_id"),
    F.col("drug_id"),
    F.col("manufacturer_id"),
    F.col("status_id"),
    F.col("first_reported_date"),
    F.col("estimated_resolution_date"),
    F.col("actual_resolution_date"),
    F.col("export_date").alias("last_updated_date"),
    F.when(F.col("change_type") != "resolved", True).otherwise(False).alias("is_current")
)

# Write dimension tables
dim_drug.write.mode("overwrite").parquet(f"s3://{args['gold_bucket']}/dimensions/dim_drug/")
dim_manufacturer.write.mode("overwrite").parquet(f"s3://{args['gold_bucket']}/dimensions/dim_manufacturer/")
dim_status.write.mode("overwrite").parquet(f"s3://{args['gold_bucket']}/dimensions/dim_status/")

# Write fact table
fact_shortages.write.mode("overwrite").partitionBy("last_updated_date").parquet(f"s3://{args['gold_bucket']}/facts/fact_shortages/")

job.commit()
