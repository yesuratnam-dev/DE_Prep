# bronze.py
import os
import io
import json
import zipfile
import requests
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.session import get_fda_manifest_node

# Container path mapped to host
BASE_OUT = "/opt/airflow/data"
DATASET_FOLDER = "drugs_fda"
PRODUCT, ENDPOINT = "drug", "drugsfda"

def download_latest_drugs_fda():
    """Download and extract FDA shortage data"""

    node,session = get_fda_manifest_node(product=PRODUCT, endpoint=ENDPOINT)

    export_date = node["export_date"]
    parts = node["partitions"]

    # 2) Make dated folder
    out_dir = os.path.join(BASE_OUT, DATASET_FOLDER, f"export_date={export_date}")
    os.makedirs(out_dir, exist_ok=True)

    # 3) Download & extract each partition
    saved = []
    for p in parts:
        url = p["file"]
        z = session.get(url, timeout=120, verify=True)
        z.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(z.content)) as zf:
            for name in zf.namelist():
                with zf.open(name) as f:
                    data = f.read()
                out_path = os.path.join(out_dir, name)
                with open(out_path, "wb") as out:
                    out.write(data)
                saved.append(out_path)

    print(f"export_date={export_date} → saved files:\n" + "\n".join(saved))
    return {"export_date": export_date, "files": saved, "total_records": node.get("total_records")}

# DAG definition
with DAG(
        dag_id="raw_data_ingestion_task_drugsfda",
        start_date=datetime(2025, 1, 1),
        schedule="@daily",
        catchup=False,
        tags=["fda", "bronze", "drugs_fda"]
) as dag:

    download_task = PythonOperator(
        task_id="download_drugs_fda",
        python_callable=download_latest_drugs_fda
    )
