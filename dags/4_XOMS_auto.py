from airflow.sdk import dag , task 

@dag(
    dag_id = "XCOM_auto"
)

def XCOM_auto():

    @task.python
    def first_task():
        fetched_data = {'data' : [1,2,3,4,5,6]}
        print(f'We are fetching data: {fetched_data}')
        return fetched_data

    @task.python
    def second_task(data:dict):
        transform_data = data['data']
        transformed_data = [x*2 for x in data['data']]
        trans_data_dict = {"data": transformed_data}
        print("This is task transformed data")
        return trans_data_dict

    @task.python
    def third_task(data:dict):
        load_data = data['data']
        print("This is the third task to load the data")
        print(f"Loaded data is : {load_data}")



    # Defining the task dependancy

    first = first_task()
    second = second_task(first)
    third = third_task(second)

    first >> second >> third


# Instancing the dag - registering the dag 

XCOM_auto()