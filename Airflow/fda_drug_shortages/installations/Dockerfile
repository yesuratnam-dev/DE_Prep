FROM apache/airflow:3.0.4-python3.12

USER root
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

USER airflow
COPY installations/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /opt/airflow/
