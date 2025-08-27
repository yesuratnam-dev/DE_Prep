"""Data ingestion script for openFDA drug shortages API."""

import json
import requests
import boto3
from datetime import datetime
import hashlib
import logging
from config.config import OPENFDA_BASE_URL, BRONZE_BUCKET, API_LIMIT, MAX_RETRIES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ingest_fda_data(execution_date: str) -> bool:
    """
    Ingest FDA drug shortage data and store in S3 bronze layer.
    
    Args:
        execution_date: Execution date in YYYY-MM-DD format
        
    Returns:
        bool: True if successful, False otherwise
    """
    s3_client = boto3.client('s3')
    
    try:
        # Fetch data from openFDA API
        url = f"{OPENFDA_BASE_URL}?limit={API_LIMIT}"
        
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                break
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == MAX_RETRIES - 1:
                    raise
        
        data = response.json()
        
        # Add metadata
        enriched_data = {
            'export_date': execution_date,
            'ingestion_timestamp': datetime.utcnow().isoformat(),
            'record_count': len(data.get('results', [])),
            'data_hash': hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest(),
            'results': data.get('results', [])
        }
        
        # Upload to S3 bronze layer
        s3_key = f"raw/{execution_date}/shortages.json"
        s3_client.put_object(
            Bucket=BRONZE_BUCKET,
            Key=s3_key,
            Body=json.dumps(enriched_data, indent=2),
            ContentType='application/json'
        )
        
        logger.info(f"Successfully ingested {enriched_data['record_count']} records to s3://{BRONZE_BUCKET}/{s3_key}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to ingest FDA data: {e}")
        return False
