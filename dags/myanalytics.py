from time import sleep
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# Default parameters
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 9, 1),
    "retries": 0,
    "retry_delay": timedelta(minutes=2)
}

schedule = None

# Declare dag.
dag = DAG("myanalytics", default_args=default_args, schedule_interval=schedule)


t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)
t2_1 = BashOperator(task_id="random_failure_2_1", bash_command="python3 /app/random_failure_app.py 0.0", dag=dag)
t2_2 = BashOperator(task_id="random_failure_2_2", bash_command="python3 /app/random_failure_app.py 0.8", dag=dag)
t2_3 = BashOperator(task_id="random_failure_2_3", bash_command="python3 /app/random_failure_app.py 0.0", dag=dag)
t3 = BashOperator(task_id="random_failure_4", bash_command="python3 /app/random_failure_app.py 0.0", dag=dag)

#
# Set dependencies.
#
t1 >> [t2_1, t2_2, t2_3]

[t2_1, t2_2, t2_3] >> t3
