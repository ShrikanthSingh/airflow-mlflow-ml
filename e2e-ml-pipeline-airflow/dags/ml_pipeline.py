from airflow.models import DAG

from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime

from utils.load_data import load_data
from utils.preprocess_data import preprocess_data
from utils.experiment import experiment
from utils.track_experiments_info import track_experiments_info
from utils.fit_best_model import fit_best_model
from utils.save_batch_data import save_batch_data
from utils.custom_metrics import log_all_eval_metrics


default_args= {
    'owner': 'Shrikanth Singh',
    'email_on_failure': False,
    'start_date': datetime(2022, 12, 22)
}

with DAG(
    "ml_pipeline",
    description='End-to-end ML pipeline example',
    schedule_interval='@daily',
    default_args=default_args, 
    catchup=False) as dag:

    # task_0
    dummy_start = DummyOperator(
        task_id='Start_Dag',
    )

    # task: 1
    with TaskGroup('creating_storage_structures') as creating_storage_structures:

        # task: 1.1
        creating_experiment_tracking_table = PostgresOperator(
            task_id="creating_experiment_tracking_table",
            postgres_conn_id='postgres_default',
            sql='sql/create_experiments.sql'
        )

        # task: 1.2
        creating_batch_data_table = PostgresOperator(
            task_id="creating_batch_data_table",
            postgres_conn_id='postgres_default',
            sql='sql/create_batch_data_table.sql'
        )

    # task: 2
    fetching_data = PythonOperator(
        task_id='fetching_data',
        python_callable=load_data

    )
    
    # task: 3
    with TaskGroup('preparing_data') as preparing_data:

        # task: 3.1
        preprocessing = PythonOperator(
            task_id='preprocessing',
            python_callable=preprocess_data
        )

        # task: 3.2
        saving_batch_data = PythonOperator(
            task_id='saving_batch_data',
            python_callable=save_batch_data
        )
        
    # task: 4
    hyperparam_tuning = PythonOperator(
        task_id='hyperparam_tuning',
        python_callable=experiment
    )

    # task: 5
    with TaskGroup('after_crossvalidation') as after_crossvalidation:

        # =======
        # task: 5.1        
        saving_results = PythonOperator(
            task_id='saving_results',
            python_callable=track_experiments_info
        )

        # task: 5.2
        fitting_best_model = PythonOperator(
            task_id='fitting_best_model',
            python_callable=fit_best_model
        )  

    # task_0
    dummy_end = DummyOperator(
        task_id='End_Dag',
    )

    dummy_start >> \
    creating_storage_structures >> \
    fetching_data >> preparing_data >> \
    hyperparam_tuning >> \
    after_crossvalidation >> \
    dummy_end