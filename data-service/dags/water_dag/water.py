import airflow
from airflow import DAG
from water_dag.tasks.fetch_water_data import fetch_water_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(7),
}

with DAG(
    'water_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as snow_dag:
    
    fetch_water_data_task = fetch_water_data()

    # TODO: add task dependencies

    