from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 24),
    'retries': 1,
}

with DAG(
    'etl_sales_data',
    default_args=default_args,
    description='ETL pipeline for sales_data',
    schedule='@daily',  # runs every day
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id='run_etl_script',
        bash_command='.venv/bin/python'
        ' src/main.py'                   #  'C:\\Users\\Gita\\OneDrive\\Documents\\ETL_Project\\scripts\\etl_process.py'
    )