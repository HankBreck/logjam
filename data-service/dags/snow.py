import os
from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

dag_path = os.getcwd()

# TODO: Setup first DAG to pull snow data
    # https://www.youtube.com/watch?v=2nhdhIYueIE
