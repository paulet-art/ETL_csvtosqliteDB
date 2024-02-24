from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import PythonOperator

default_args = {
    'owner' : 'admin',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id = 'dag',
    default_args=default_args,
    description= "firstdag",
    start_date=datetime(2024, 2,18),
    schedule='@daily'
) as dag:
    
    task = PythonOperator(
        task_id = "first_task",
        bash_command= "echo this is the first task",
        dag=dag
    )