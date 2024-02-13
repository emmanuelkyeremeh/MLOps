import datetime
import time
import logging
import pandas as pd
import psycopg
import pickle
from prefect import task, flow

from evidently.report import Report
from evidently import ColumnMapping
from evidently.metrics import ColumnDriftMetric, DatasetDriftMetric, DatasetMissingValuesMetric

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s")

SEND_TIMEOUT = 10

create_table_statement = """
drop table if exists nba_salary_model_metrics;
create table nba_salary_model_metrics(
    timestamp timestamp,
    prediction_drift float,
    num_drifted_columns integer,
    share_missing_values float
)
"""
reference_data = pd.read_csv("data/reference.csv")
with open('models/nba_salaries_predictor_v2.bin', 'rb') as file:
    model = pickle.load(file)

raw_data = pd.read_csv("data/raw.csv")

begin = datetime.datetime(2024, 2, 1, 0, 0)

num_features = ['Age', 'GP', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF',
                'PTS', 'Total Minutes', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']

cat_features = ['position_C', 'position_PF', 'position_PG', 'position_PG-SG',
                'position_SF', 'position_SF-PF', 'position_SF-SG', 'position_SG', 'position_SG-PG']

column_mapping = ColumnMapping(
    prediction='prediction',
    numerical_features=num_features,
    categorical_features=cat_features,
    target=None
)

report = Report(metrics=[
    ColumnDriftMetric(column_name='prediction'),
    DatasetDriftMetric(),
    DatasetMissingValuesMetric()
])


@task
def prep_db():
    with psycopg.connect("host=localhost port=5432 user=postgres password=0507", autocommit=True) as conn:
        res = conn.execute(
            "SELECT 1 FROM pg_database WHERE datname='ml_monitoring'")
        if len(res.fetchall()) == 0:
            conn.execute("create database ml_monitoring;")
        with psycopg.connect("host=localhost port=5432 dbname=ml_monitoring user=postgres password=0507") as conn:
            conn.execute(create_table_statement)


@task
def calculate_metrics_postgresql(curr, i):

    raw_data['prediction'] = model.predict(
        raw_data[num_features + cat_features])

    report.run(reference_data=reference_data,
               current_data=raw_data, column_mapping=column_mapping)

    result = report.as_dict()

    prediction_drift = result['metrics'][0]['result']['drift_score']
    num_drifted_columns = result['metrics'][1]['result']['number_of_drifted_columns']
    share_missing_values = result['metrics'][2]['result']['current']['share_of_missing_values']

    curr.execute(
        "insert into nba_salary_model_metrics(timestamp, prediction_drift, num_drifted_columns, share_missing_values) values (%s, %s, %s, %s)",
                (begin + datetime.timedelta(i), prediction_drift,
                 num_drifted_columns, share_missing_values)
    )


@flow
def batch_monitoring_backfill():
    prep_db()
    last_send = datetime.datetime.now() - datetime.timedelta(seconds=10)
    with psycopg.connect("host=localhost port=5432 dbname=ml_monitoring user=postgres password=0507", autocommit=True) as conn:
        for i in range(0, 27):
            with conn.cursor() as curr:
                calculate_metrics_postgresql(curr, i)

            new_send = datetime.datetime.now()
            seconds_elapsed = (new_send - last_send).total_seconds()
            if seconds_elapsed < SEND_TIMEOUT:
                time.sleep(SEND_TIMEOUT - seconds_elapsed)
            while last_send < new_send:
                last_send = last_send + datetime.timedelta(seconds=10)
            logging.info("data sent")


if __name__ == '__main__':
    batch_monitoring_backfill()
