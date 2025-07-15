from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 15, 0, 0),  # Start date (adjust as needed)
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='dataflow_flex_batch_5min_schedule_dag_no_build',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),  # Schedule every 5 minutes
    catchup=False,  # Set to False to avoid historical runs
    tags=['dataflow', 'flex-template', 'batch'],
) as dag:
    # Task to run the Dataflow Flex Template
    run_dataflow_flex_template = BashOperator(
        task_id='run_dataflow_batch_flex_template_job',
        bash_command="""
              gcloud dataflow flex-template run "flex-`date +%Y%m%d-%H%M%S`" \
                --template-file-gcs-location "gs://getwellsoon-bucket-demo/templates/getting_started_py.json" \
                --region $REGION \
                --parameters output="gs://getwellsoon-bucket-demo/templates/output-`date +%Y%m%d-%H%M%S`"
                    """,
    )



# from airflow import DAG
# from datetime import datetime, timedelta
# from airflow.operators.bash import BashOperator

# with DAG(
#     dag_id="my_5_minute_dag_timedelta",
#     start_date=datetime(2025, 7, 1),
#     schedule_interval=timedelta(minutes=5),  # Runs every 5 minutes
#     catchup=False,
# ) as dag:
#     task_1 = BashOperator(
#         task_id="run_every_five_minutes_task",
#         bash_command="echo 'This DAG is running every 5 minutes!'"
#     )
