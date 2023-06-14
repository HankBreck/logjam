import airflow
from airflow import DAG
from snow_dag.tasks.fetch_snow_data import fetch_snow_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(7),
}

with DAG(
    'snow_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as snow_dag:
    
    fetch_snow_data_task = fetch_snow_data()

    # TODO: add task dependencies

    