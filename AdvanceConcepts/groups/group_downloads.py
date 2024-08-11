from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup


def download_tasks():
  with TaskGroup("downloads", toolpit='Download tasks') as group:
    # group_id, toolpit when you hover on GUI

    download_a = BashOperator(
        task_id='download_a',
        bash_command='sleep 10'
    )
 
    download_b = BashOperator(
        task_id='download_b',
        bash_command='sleep 10'
    )
 
    download_c = BashOperator(
        task_id='download_c',
        bash_command='sleep 10'
    )

    return group