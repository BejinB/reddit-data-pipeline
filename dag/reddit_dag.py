import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add /opt/airflow to sys.path to make pipelines available
sys.path.append('/opt/airflow')

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline


default_args = {
    'owner': 'BejinB',
    'start_date': datetime(2023, 10, 22)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    do_xcom_push=True,
    dag=dag
)

# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3
