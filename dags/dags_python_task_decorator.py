from airflow.decorators import dag
from airflow.decorators import task
import pendulum

@dag(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
@task(task_id="python_task_1")
def print_context(ds=None, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    print(kwargs)
    print(ds)
    return "Whatever you return gets printed in the logs"

python_task_1 = print_context(ds='Run task decorator')