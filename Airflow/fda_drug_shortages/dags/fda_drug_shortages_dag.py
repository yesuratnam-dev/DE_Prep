"""Airflow DAG for FDA Drug Shortages data pipeline."""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
import sys
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from scripts.ingest_data import ingest_fda_data

default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'fda_drug_shortages_pipeline',
    default_args=default_args,
    description='FDA Drug Shortages data pipeline',
    schedule_interval='0 2 * * *',  # Daily at 2 AM UTC
    catchup=False,
    max_active_runs=1
)

# Task 1: Ingest data from openFDA API
ingest_task = PythonOperator(
    task_id='ingest_fda_data',
    python_callable=ingest_fda_data,
    op_kwargs={'execution_date': '{{ ds }}'},
    dag=dag
)

# Task 2: Check if file was successfully uploaded
file_sensor = S3KeySensor(
    task_id='check_bronze_file',
    bucket_name='{{ var.value.bronze_bucket }}',
    bucket_key='raw/{{ ds }}/shortages.json',
    timeout=3600,
    poke_interval=60,
    dag=dag
)

# Task 3: Process Bronze to Silver
bronze_to_silver = GlueJobOperator(
    task_id='bronze_to_silver',
    job_name='fda-bronze-to-silver',
    script_args={
        '--export_date': '{{ ds }}',
        '--bronze_bucket': '{{ var.value.bronze_bucket }}',
        '--silver_bucket': '{{ var.value.silver_bucket }}'
    },
    dag=dag
)

# Task 4: Process Silver to Gold
silver_to_gold = GlueJobOperator(
    task_id='silver_to_gold',
    job_name='fda-silver-to-gold',
    script_args={
        '--export_date': '{{ ds }}',
        '--silver_bucket': '{{ var.value.silver_bucket }}',
        '--gold_bucket': '{{ var.value.gold_bucket }}'
    },
    dag=dag
)

# Define task dependencies
ingest_task >> file_sensor >> bronze_to_silver >> silver_to_gold
