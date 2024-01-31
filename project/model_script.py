import pandas as pd
from prefect import task, flow
import mlflow


@task
def read_dataframe(filename):
    dataframe = pd.read_csv(f"./data/{filename}")
    return dataframe


@task
def clean_dataframe(dataframe):
    null_columns = dataframe.columns[dataframe.isnull().any()]
    dataframe[null_columns] = dataframe[null_columns].fillna(0.000)

    dataframe = dataframe.drop(columns=['Unnamed: 0'])
    dummies = pd.get_dummies(
        dataframe["Position"], prefix="position").astype('int')

    dataframe = dataframe.drop(
        columns=["Player Name", "Position", "Team", "Salary"])
    dataframe = pd.concat([dataframe, dummies], axis=1)

    return dataframe


@task
def load_model(run_id):
    mlflow.set_tracking_uri(
        "http://ec2-54-227-30-175.compute-1.amazonaws.com:5000")
    mlflow.set_experiment("my-nba-salary-experiment")

    logged_model = f"runs:/{run_id}/models"
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    return loaded_model


@flow
def apply(df_filename, run_id):
    loaded_data = read_dataframe(df_filename)

    X = clean_dataframe(loaded_data)

    model = load_model(run_id)

    prediction = model.predict(X)

    print(prediction)


if __name__ == "__main__":
    apply(df_filename="nba_2022-23_all_stats_with_salary.csv",
          run_id="e1c559f73689441aa181e4f195690e54")
