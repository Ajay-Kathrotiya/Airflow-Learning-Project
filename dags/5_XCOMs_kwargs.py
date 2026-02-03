from airflow.sdk import dag , task 

@dag(
    dag_id = "XCOM_kwargs"
)

def XCOM_kwargs():

    @task.python
    def first_task(**kwargs):

        # Extracting 'ti' from kwargs to push XCOM manually.

        ti = kwargs['ti']
        fetched_data = {'data' : [1,2,3,4,5,6]}
        print(f'We are fetching data: {fetched_data}')
        ti.xcom_push(key='return_value',value = fetched_data)

    @task.python
    def second_task(**kwargs):

        ti = kwargs['ti']
       
        # Extracting pulling xcom :

        fetched_data =  ti.xcom_pull(task_ids = 'first_task' , key = "return_value")['data']
        transformed_data = [x*2 for x in fetched_data]
        trans_data_dict = {"data": transformed_data}
        print("This is task transformed data")
        
        ti.xcom_push(key = 'return_value',value = trans_data_dict)
        

    @task.python
    def third_task(**kwargs):
        ti =kwargs['ti']
        load_data = ti.xcom_pull(task_ids = 'second_task', key = "return_value")
        print("This is the third task to load the data")
        print(f"Loaded data is : {load_data}")



    # Defining the task dependancy

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third


# Instancing the dag - registering the dag 

XCOM_kwargs()