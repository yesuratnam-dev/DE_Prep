"""Configuration settings for FDA Drug Shortages pipeline."""

import os

# S3 Configuration
BRONZE_BUCKET = os.getenv('BRONZE_BUCKET', 'fda-shortages-bronze')
SILVER_BUCKET = os.getenv('SILVER_BUCKET', 'fda-shortages-silver')
GOLD_BUCKET = os.getenv('GOLD_BUCKET', 'fda-shortages-gold')

# API Configuration
OPENFDA_BASE_URL = 'https://api.fda.gov/drug/shortage.json'
API_LIMIT = 1000

# Database Configuration
GLUE_DATABASE = 'fda_drug_shortages_db'
METADATA_TABLE = 'pipeline_metadata'

# Processing Configuration
BATCH_SIZE = 100
MAX_RETRIES = 3
