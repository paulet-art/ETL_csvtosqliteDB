from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'admin',
    'retries' : 5,
    'retry_delay':timedelta(minutes=2)
    }

with DAG(
    dag_id='dag',
    default_args=default_args,
    description='my first dag',
    start_date=datetime(2024,2,1,10),
    schedule='@daily'
) as  dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command= "echo this is the first task",
        dag=dag
    )
    task2 = BashOperator(
        task_id = "second_task",
        bash_command= "echo this is the second task,running after first task",
        dag=dag
    )
    task3 = BashOperator(
        task_id = "third_task",
        bash_command= "echo i will run at same time as task2",
        dag=dag
    )
task1.set_downstream(task2) # or task 1 >> task2
task1.set_downstream(task3) # or task1 >> task3