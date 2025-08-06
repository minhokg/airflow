from airflow import DAG
import pendulum
import datetime
from airflow.decorators import dag
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz='UTC'),
    catchup=False
) as dag:
    
    regist = PythonOperator(
        task_id = "regist",                                  
        python_callable=regist,
        op_args=['minhokg','man','kr','seoul'],
        op_kwargs={'email':'minho.kg97@gmail.com','phone':'015754719674'},
        )

    regist