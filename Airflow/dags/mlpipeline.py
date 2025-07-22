from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#Define our task 1
def preprocess_data():
    print("Preprocessing data...")

#Define our task 2
def train_model():
    print("Training model...")

#Define our task 3
def evaluate_model():
    print("Evaluate Models...")

#Define the DAG
with DAG(
    dag_id='ml_pipeline',
    start_date=datetime(2024,1,1),
    schedule='@weekly',
) as dag:
    
    #Define the task
    preprocess = PythonOperator(task_id="preprocess_task",
                                python_callable=preprocess_data)
    train = PythonOperator(task_id="train_task",
                           python_callable=train_model)
    evaluate = PythonOperator(task_id="evaluate_task",
                              python_callable=evaluate_model)
    
    # Set the dependencies
    preprocess >> train >> evaluate


[
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_customers_dataset.csv",
        "file_name": "olist_customers_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_geolocation_dataset.csv",
        "file_name": "olist_geolocation_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_order_items_dataset.csv",
        "file_name": "olist_order_items_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_order_reviews_dataset.csv",
        "file_name": "olist_order_reviews_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_orders_dataset.csv",
        "file_name": "olist_orders_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_products_dataset.csv",
        "file_name": "olist_products_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_sellers_dataset.csv",
        "file_name": "olist_sellers_dataset.csv"
    },
    {
        "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/product_category_name_translation.csv",
        "file_name": "product_category_name_translation.csv"
    }

]