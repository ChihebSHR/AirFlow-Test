from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def process_image():
    # Your image processing code here
    # Extract information from the image
    
    # Example: Print a message
    print("Image processing completed!")

# Define the DAG
dag = DAG(
    dag_id='image_processing_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='0 0 * * *'  # Runs once daily at midnight
)

# Define the task
process_image_task = PythonOperator(
    task_id='process_image',
    python_callable=process_image,
    dag=dag
)

# Set the task dependency
process_image_task

