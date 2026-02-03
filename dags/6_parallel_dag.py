from airflow.sdk import dag , task 
from datetime import datetime

@dag(
    dag_id = "parallel_dag",
    schedule="@daily",
    start_date = datetime(2024,1,1),
    catchup = False
)

def parallel_dag():

    @task.python
    def extract_task(**kwargs):
        print("This is the first task Extracting data....")
        extracted_data_dict = {"api_extracted_data": [1,2,3],
                          "db_extracted_data":[4,5,6],
                          "s3_extracted_data" : [7,8,9]}
        ti = kwargs['ti']
        ti.xcom_push(key = "return_value", value = extracted_data_dict)

    @task.python
    def transform_task_api(**kwargs):
        print("This is the second task for transformt the data...")
        ti = kwargs['ti']
        api_extracted_data = ti.xcom_pull(task_ids = 'extract_task', key = 'return_value')['api_extracted_data']
        api_extracted_data = [x*10 for x in api_extracted_data]
        ti.xcom_push(key = 'return_value', value = api_extracted_data)
        
    @task.python
    def tranform_task_db(**kwargs):
        print("Db transfomr taks")
        ti = kwargs['ti']
        db_extracted_data = ti.xcom_pull(task_ids = 'extract_task',key = 'return_value')['db_extracted_data']
        db_extracted_data = [x*200 for x in db_extracted_data]
        print(db_extracted_data)
        ti.xcom_push(key='return_value',value = db_extracted_data)

    @task.python
    def transform_task_s3(**kwargs):
        print("Trandforming s3 data...")
        ti = kwargs['ti']
        s3_data = ti.xcom_pull(task_ids = 'extract_task',key = 'return_value')['s3_extracted_data']
        s3_trasnformed_data  = [x*1000 for x in s3_data]
        ti.xcom_push(key = 'return_value', value = s3_trasnformed_data)

    @task.bash
    def load_data(**kwargs):
        print('Loading data....')
        api_data = kwargs['ti'].xcom_pull(task_ids = 'transform_task_api')
        db_data = kwargs['ti'].xcom_pull(task_ids = 'tranform_task_db')
        s3_data= kwargs['ti'].xcom_pull(task_ids = 'transform_task_s3')

        return f" echo 'data is {api_data},{db_data},{s3_data}'"


    # Defining the task dependancy

    extract = extract_task()
    transform_task_api = transform_task_api()
    tranform_task_db = tranform_task_db()
    transform_task_s3 = transform_task_s3()
    load = load_data()

    extract >> [transform_task_api,tranform_task_db,transform_task_s3] >> load


# Instancing the dag - registering the dag 

parallel_dag()