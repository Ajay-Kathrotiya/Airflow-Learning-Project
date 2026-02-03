from airflow.sdk import dag , task 
from pendulum import datetime

@dag(
    dag_id = "first_schedule_cron",
    start_date=datetime(year=2026,month=2,day=1,tz="Asia/Kolkata"),
    schedule="*/3 * * * *",
    is_paused_upon_creation=True,
    catchup=False

)

def first_schedule_cron():

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

first_schedule_cron()