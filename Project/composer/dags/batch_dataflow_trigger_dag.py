from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="my_5_minute_dag_timedelta",
    start_date=datetime(2025, 7, 1),
    schedule_interval=timedelta(minutes=5),  # Runs every 5 minutes
    catchup=False,
) as dag:
    task_1 = BashOperator(
        task_id="run_every_five_minutes_task",
        bash_command="echo 'This DAG is running every 5 minutes!'"
    )
