"""Glue ETL script to transform bronze to silver layer."""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import *
import hashlib

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'export_date', 'bronze_bucket', 'silver_bucket'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

def generate_shortage_id(drug_name, manufacturer_name, ndc):
    """Generate deterministic shortage ID."""
    key = f"{drug_name}_{manufacturer_name}_{ndc}".lower()
    return hashlib.md5(key.encode()).hexdigest()

def detect_changes(current_df, previous_df):
    """Detect changes between current and previous day data."""
    if previous_df is None:
        return current_df.withColumn("change_type", F.lit("new"))
    
    # Join current with previous to detect changes
    joined = current_df.alias("current").join(
        previous_df.alias("previous"),
        on="shortage_id",
        how="full_outer"
    )
    
    # Determine change type
    change_type = F.when(
        F.col("previous.shortage_id").isNull(), "new"
    ).when(
        F.col("current.shortage_id").isNull(), "resolved"
    ).when(
        F.col("current.status") != F.col("previous.status"), "updated"
    ).otherwise("unchanged")
    
    return joined.select("current.*").withColumn("change_type", change_type)

# Read current day's data
current_path = f"s3://{args['bronze_bucket']}/raw/{args['export_date']}/shortages.json"
current_raw = spark.read.json(current_path)

# Flatten and transform data
current_df = current_raw.select(
    F.explode("results").alias("shortage")
).select(
    F.col("shortage.drug_name").alias("drug_name"),
    F.col("shortage.ndc").alias("ndc"),
    F.col("shortage.manufacturer_name").alias("manufacturer_name"),
    F.col("shortage.status").alias("status"),
    F.col("shortage.shortage_reason").alias("shortage_reason"),
    F.col("shortage.related_treatments").alias("related_treatments"),
    F.to_date(F.col("shortage.first_reported_date")).alias("first_reported_date"),
    F.to_date(F.col("shortage.estimated_resolution_date")).alias("estimated_resolution_date"),
    F.to_date(F.col("shortage.actual_resolution_date")).alias("actual_resolution_date"),
    F.lit(args['export_date']).alias("export_date")
).withColumn(
    "shortage_id",
    F.udf(generate_shortage_id, StringType())(
        F.col("drug_name"), F.col("manufacturer_name"), F.col("ndc")
    )
)

# Try to read previous day's data for change detection
try:
    from datetime import datetime, timedelta
    prev_date = (datetime.strptime(args['export_date'], '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    prev_path = f"s3://{args['silver_bucket']}/processed/export_date={prev_date}/"
    previous_df = spark.read.parquet(prev_path)
except:
    previous_df = None

# Detect changes
final_df = detect_changes(current_df, previous_df)

# Write to silver layer
output_path = f"s3://{args['silver_bucket']}/processed/"
final_df.write.mode("overwrite").partitionBy("export_date").parquet(output_path)

job.commit()
