from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.etl_script import etl_process
import os

# default dag
default_args={
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 24),
    'retries': 1
}

# dag
with DAG (
    dag_id = 'csvtosqlitedb',
    default_args=default_args,
    description= "fraud data to sqlitedb",
    start_date=datetime(2024, 2, 18),
    schedule='@daily'
) as dag:
    
    # task
    etl_task= PythonOperator(
    task_id='etl_process',
    python_callable=etl_process,
    dag=dag,
    )

# dependencies
etl_task