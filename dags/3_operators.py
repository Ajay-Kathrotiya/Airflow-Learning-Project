from airflow.decorators import dag, task 
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

@dag(
    dag_id ="operators",
    start_date = datetime(2025,2,3),
    schedule = '@daily',
    catchup = False
)

def operators():

    @task.bash
    def task_1():
        return "echo this is ajay"
    
    @task.python
    def task_2():
        print("This is task 2 python task")

    run_this = BashOperator(
    task_id="run_after_loop",
    bash_command="echo https://airflow.apache.org/",
    )


    
    first = task_1()
    second = task_2()
    third = run_this


    first >> second >> third

operators()
