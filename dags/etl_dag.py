from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='ETL Pipeline for processing customer data',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

run_etl = BashOperator(
    task_id='run_etl',
    # Airflow's BashOperator allows you to execute a bash command or script as part of your DAG. In this case, we are using it to run the main.py script that contains our ETL pipeline. The command 'python ../src/main.py' tells Airflow to execute the main.py script located in the src directory, which is one level up from the dags directory where this DAG file is located.
    # Normally its best practice to use absolute paths in Airflow because the BashOperator runs the command on the worker machine, not inside the editor. But its not portable so I opted into a relative path in case of the repo being cloned.
    # if it was to be an absolute path, it would look something like this:
    # bash_command='python /Users/anouk/Projects/ETL-Pipeline/src/main.py',
    bash_command='python ../src/main.py',
    dag=dag,
)