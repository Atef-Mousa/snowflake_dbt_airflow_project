# import os
# import yaml
# import sys
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# import snowflake.connector
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'email': ['atefatef648@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

#
with DAG(
    dag_id='order_monitoring_dag16',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='source "/home/atef/dbt_env/bin/activate" && cd "/home/atef/project/E-Commerce-Order-Pipeline/dbt_ecommerce" && dbt run'
        # bash_command='source "/Users/zafarimam/Documents/E-Commerce Order Pipeline/airflow_venv_39/bin/activate" && cd "/Users/zafarimam/Documents/E-Commerce Order Pipeline/dbt_ecommerce" && dbt run'

    )

    check_orders = BashOperator(
    task_id='check_delayed_orders',
    bash_command='source /home/atef/project/E-Commerce-Order-Pipeline/airflow_venv_39/bin/activate && python /home/atef/project/E-Commerce-Order-Pipeline/airflow_project/dags/utils/check_delayed_orders.py',
    email_on_failure=True,
    )
    # check_orders = BashOperator(
    #     task_id='check_delayed_orders',
    #     bash_command='source "/home/atef/project/E-Commerce-Order-Pipeline/airflow_venv_39/bin/activate" && python "/home/atef/project/E-Commerce-Order-Pipeline/airflow_project/dags/utils/check_delayed_orders.py"'
    # )

    dbt_run >> check_orders