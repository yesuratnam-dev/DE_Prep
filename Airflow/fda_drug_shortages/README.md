# FDA Drug Shortages Data Pipeline

Automated data pipeline for ingesting, processing, and analyzing FDA drug shortage data from openFDA API.

## Architecture
- **Bronze Layer**: Raw JSON data from openFDA API
- **Silver Layer**: Processed data with change detection
- **Gold Layer**: Dimensional model for analytics
- **Orchestration**: Airflow DAGs

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run the DAG
airflow dags trigger fda_drug_shortages_pipeline
```

## Components
- `dags/`: Airflow DAG definitions
- `scripts/`: ETL processing scripts
- `config/`: Configuration files
- `tests/`: Unit and integration tests
