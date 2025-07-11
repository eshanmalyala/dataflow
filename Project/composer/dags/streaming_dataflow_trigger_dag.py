from airflow import models
from airflow.providers.google.cloud.operators.dataflow import DataflowStartFlexTemplateOperator
from datetime import datetime

PROJECT_ID = "gcp-agent-garden"
REGION = "europe-west1"
TEMPLATE_GCS_PATH = "gs://getwellsoon-bucket-demo/templates/streaming_pipeline.json"
SUBSCRIPTION = f"projects/{PROJECT_ID}/subscriptions/getwellsoon-topic-sub"
BQ_TABLE = f"{PROJECT_ID}:getwellsoon_dataset.customer_data"

SUBNETWORK = f"https://www.googleapis.com/compute/v1/projects/{PROJECT_ID}/regions/{REGION}/subnetworks/dataflow-subnet"

with models.DAG(
    dag_id="trigger_streaming_dataflow_job",
    schedule_interval=None,
    start_date=datetime(2025, 7, 10),
    catchup=False,
    tags=["streaming", "dataflow", "pii"],
) as dag:

    start_streaming_job = DataflowStartFlexTemplateOperator(
        task_id="start_streaming_flex_job",
        project_id=PROJECT_ID,
        location=REGION,
        body={
            "launchParameter": {
                "jobName": "streaming-pii-job-{{ ds_nodash }}",
                "containerSpecGcsPath": TEMPLATE_GCS_PATH,
                "parameters": {
                    "input_subscription": SUBSCRIPTION,
                    "output_table": BQ_TABLE
                },
                "environment": {
                    "subnetwork": SUBNETWORK,
                    "ipConfiguration": "WORKER_IP_PRIVATE"
                }
            }
        }
    )
