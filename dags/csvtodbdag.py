from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# default dag
default_args={
    'owner': 'admin',
    'catchup' : True,
    'retries': 5,
    'retry_delay' : timedelta(minutes=5)
}

# import etl_process() 
def etl_process():
    from scripts.etl_script import etl_process
    etl_process()

# dag
with DAG (
    dag_id = 'ETL_csvtodb',
    default_args=default_args,
    description= "etl dag",
    start_date=datetime(2024, 2, 18, 0, 0, 0),
    schedule='@daily'
) as dag:
    
    etl_task = PythonOperator(
    task_id='etl_process',
    python_callable=etl_process,
    dag=dag,
)

# dependencies
etl_task