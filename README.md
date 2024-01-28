# **MlOps Project Repo**

### A repo for all projects completed as part of the [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) course

### Collaborators

- **[Silas](https://github.com/Silas-Asamoah)**
- **[Moses](https://github.com/mosesRGT)**
- **[Emmanuel](https://github.com/emmanuelkyeremeh)**

## Prefect Deployment

- Created two MLflow runs using the Lasso model and XGBoost respectively

![Screenshot (69)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/0ed83c6f-e0bb-4dc4-a4e2-323dcd4fac2b)
![Screenshot (68)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/53725fdf-6201-410d-a42d-3d638160cc83)

- Created `create_s3_bucket_block.py` which creates aws ans s3 credentials inside of prefect to facilitate the deployment of mlflow runs which have been converted to prefect flows

![Screenshot (70)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/22317be9-f9c3-4dc3-82c1-445c99083a99)

- Added `orchestrate_s3.py` which converts the previously created mlflow runs into flows using prefect with the artifacts from each run stored inside an S3 bucket in AWS.

![Screenshot (78)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/b85f35af-e148-49fa-b2e6-ae2093b68d68)
![Screenshot (77)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/ae22b913-b78f-4342-9396-38a913357e1f)
![Screenshot (76)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/48238f47-1181-4d22-a913-6b5a104413ed)

- In the code below, I create `random-forest.ipynb` which is a Random Forest Regression model which is uploaded to an S3 bucket and is later utilized in `predict.py`.

  ![Screenshot (80)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/ab7cdabb-421a-4e31-a808-e80dde0acd13)

- Created `predict.py` which is a Flask app which loads the model directly from S3, prepares the features from the payload recieved from the post request and returns the predicted value for the duration

  ![Screenshot (79)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/db0ad607-563c-4db5-a537-d62065e899cf)

- The endpoint `/predict` inside of `predict.py` is tested using `test.py` below

  ![Screenshot (81)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/237525fb-3d10-410b-bfab-c2486fc17035)

- I created a `Dockerfile` which allows me to deploy the Flask app as a Docker Image.

  ![Screenshot (82)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/baafeb9b-5104-495d-b494-3200109095e5)

- The Dockerfile requires a `requirements.txt` file as shown below:

  ![Screenshot (83)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/41f8d4d8-52c9-4926-bbd3-f0cd7c8827bb)

- I updated the `.gitignore` file as shown below:

  ![Screenshot (84)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/484240b5-55c8-4c0e-8c69-098079137b76)
