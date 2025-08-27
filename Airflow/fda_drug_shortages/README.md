# FDA Drug Shortages Data Pipeline

Automated data pipeline for ingesting, processing, and analyzing FDA drug shortage data from openFDA API.

## Architecture
- **Bronze Layer**: Raw JSON data from openFDA API
- **Silver Layer**: Processed data with change detection
- **Gold Layer**: Dimensional model for analytics
- **Orchestration**: Airflow 3.0.4 with Docker

## Setup Instructions

### Prerequisites
- Docker Desktop installed and running
- Docker Compose available

### Start Airflow Services
```bash
# Navigate to installations directory
cd Airflow/fda_drug_shortages/installations

# Start all services
docker compose up -d

# Check service status
docker compose ps
```

### Access Airflow Web UI
1. Open browser to: http://localhost:8080
2. **Username**: `admin`
3. **Password**: Find the current password by running:
   ```bash
   docker logs fda_airflow_standalone | grep "Password for user 'admin'"
   ```
   Example output:
   ```
   Simple auth manager | Password for user 'admin': xZZFA8CZBNu9zmWs
   ```

### Stop Services
```bash
docker compose down
```

## Components
- `installations/`: Docker Compose configuration
- `dags/`: Airflow DAG definitions
- `scripts/`: ETL processing scripts
- `config/`: Configuration files
- `data/`: Local data storage
- `logs/`: Airflow logs

## Notes
- Password changes on each container restart
- Data persists in Docker volumes
- Uses Airflow 3.0.4 in standalone mode for development
