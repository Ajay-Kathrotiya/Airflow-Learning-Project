from airflow.sdk import dag , task 
from pendulum import datetime

@dag(
    dag_id = "first_schedule_dag",
    start_date=datetime(year=2026,month=2,day=2,tz="Asia/Kolkata"),
    schedule="@daily",
    is_paused_upon_creation=False,
    catchup=False

)

def first_schedule_dag():

    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")

    @task.python
    def third_task():
        print("This is the third task")


    # Defining the task dependancy

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third


# Instancing the dag - registering the dag 

first_schedule_dag()