# **MlOps Project Repo**

### A repo for all projects completed as part of the [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) course

### Collaborators

- **[Silas](https://github.com/Silas-Asamoah)**
- **[Moses](https://github.com/mosesRGT)**
- **[Emmanuel](https://github.com/emmanuelkyeremeh)**

## Prefect Deployment


- I created two MLflow runs using the Lasso model and XGBoost respectively


![Screenshot (69)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/0ed83c6f-e0bb-4dc4-a4e2-323dcd4fac2b)
![Screenshot (68)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/53725fdf-6201-410d-a42d-3d638160cc83)


- I created `create_s3_bucket_block.py` which creates aws ans s3 credentials inside of prefect to facilitate the deployment of mlflow runs which have been converted to prefect flows

![Screenshot (70)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/22317be9-f9c3-4dc3-82c1-445c99083a99)

- I Added `orchestrate_s3.py` which converts the previously created mlflow runs into flows using prefect with the artifacts from each run stored inside an S3 bucket in AWS.


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


  <br/>

  ## Batch Deployment

  - `score.ipynb` contains a series of functions with the end goal of recording the prections from our model and storing that in dataframe

    ![Screenshot (86)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/5af1623f-a851-4748-b528-408ff31b12dd)
    ![Screenshot (85)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/3e74c882-a525-4ca2-b065-81e5561ebf88)

- `score.ipynb` is then converted into script which I named `score.py`. This script is then modified into a prefect flow as shown in the code below

  ![Screenshot (91)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/b4ce6e9c-c4e0-4beb-934d-647e1f116caf)
  ![Screenshot (89)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/4f12b883-704d-4b3c-9479-8cdb6fa4f42d)
  ![Screenshot (88)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/b3b7c0c4-4901-4662-8d8d-4622f8ffeffd)
  ![Screenshot (87)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/1afb76aa-2e61-40e2-af35-779b40ad04a3)

- `score.py` takes in parameters including the mlflow run id, taxi type, year and month and downloads the data from the new york taxi dataset, prepares the data, downloads the model from the S3 bucket, creates a new dataframe which stores the results of the prediction and saves the dataframe as a parquet file in local storage.

<br/>

## ML-Monitoring

I created another model based on the nyc-taxi dataset. I used data from January 2022 instead of January and February 2021, which I used for previous models. I conducted exploratory data analysis and visualisation before training the model, which was a simple linear regression model. I saved the model locally and I generated a report using evidently. The code is shown below:

![Screenshot (96)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/bf828be5-d262-470b-baeb-2c2af73571f8)
<br/>

![Screenshot (95)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/e918eced-c602-4334-a242-fd9df4b4d8ec)
<br/>

![Screenshot (106)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/263b3c94-6895-4032-a29e-da77d1dd07d5)
<br/>

![Screenshot (105)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/7c1639d1-d3b4-48c9-b1f8-92bbb2a1b03e)
<br/>

![Screenshot (104)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/8fbed2ce-514c-4a83-a64b-baa9d273de74)
<br/>

![Screenshot (103)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/ac54b90c-a937-4fc3-b1b4-eff27d55958f)
<br/>

![Screenshot (102)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/ef97dacd-3b69-4730-b897-a96ffa5943f1)
<br/>

![Screenshot (101)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/040f8758-3301-42f2-88dc-cb02d295d435)
<br/>

![Screenshot (100)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/dbb45986-11b0-4912-9682-a179d180136d)
<br/>

![Screenshot (99)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/e88b7948-5c69-4b1f-b2ea-91b75b205cdc)
<br/>

![Screenshot (98)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/678e3b35-5b09-4712-b577-c4c4b7f0414d)
<br/>

![Screenshot (97)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/50b136b6-717c-42f3-b061-e6e8c1fa8a78)

<br/>

I created two scripts `evidently_metrics_calculation.py` and `dummy_metrics_calculation.py`. both scripts create a database in my local postgres server but the former populates the database with random data while the latter populates the database with relevant data and from Februrary 2022 of the nyc taxi dataset and the script is converted into a prefect flow. The code for both scripts is shown below

### `dummy_metrics_calculation.py`

![Screenshot (108)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/66afbea7-14a5-4498-92fb-16cb90c4bea7)
![Screenshot (109)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/263933c3-8fcc-4eaa-8ece-60a34b79de48)

<br/>

### `evidently_metrics_calculation.py`

![Screenshot (112)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/d1b480ca-5429-432b-86a6-1025529e3827)
![Screenshot (110)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/71e45c08-fd33-4fb9-9f2d-3778f8f05783)
![Screenshot (114)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/49c1e34d-f64f-4a00-a602-52f30b1f5e5a)
![Screenshot (113)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/072fc6c9-dd07-4572-baff-e0dbaac864f3)

<br/>

Lastly, I generated a test suite and report using evidently as shown in the code below

![Screenshot (117)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/820a3f27-5fb4-43cc-9533-3ab338623fd8)
<br/>

![Screenshot (116)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/3dd2bab2-5639-46a2-9008-90310b1333e4)
<br/>

![Screenshot (115)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/4e2bed1d-4618-4731-9668-0ea0ced2040c)
<br/>

![Screenshot (119)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/88eb329a-4615-4b20-9bac-867b8771f582)
<br/>

![Screenshot (118)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/fb1e1a87-f523-40b6-8a9a-92f6e9877719)

<br/>

## Best Practices

The `infrastructure` folder contains the `modules` folder and the `vars` folder as well as the `main.tf` , `variables.tf` and the `.terraform.lock.hcl` The main.tf file is root of the folder where an s3 bucket and two kinsesis data streams are created. The bucket and the data streams are referenced from the `kinesis` and `s3` folders inside of the `modules` folder.
`main.tf` is shown below

![Screenshot (120)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/a6864862-6b60-472e-98be-a852c8ba8ac4)

inside of `main.tf`, variables are initialized inside of `variables.tf` as shown below:

![Screenshot (121)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/fbe1fc82-a2de-4d35-99f8-973aa075050b)

Terraform automatically creates `.terraform.locl.hcl` after initializing the project as shown

![Screenshot (122)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/d6a9d6cd-fd7e-442a-904a-a11edf714c36)

The variables which were created in `variables.tf` have to be provided in the terminal when running the terraform workflow. to circumvent that, the required variables are created in the `stg.tfvars` inside of the `vars` folder as shown:

![Screenshot (123)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/22862e44-e8f0-40c2-856c-e00794c0f4d6)

Both folders inside of the `modules` folder contain a `main.tf` and a `variables.tf` file.

For the `kinesis` file, both files are shown below:

### `main.tf`

![Screenshot (124)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/15d84eef-09b5-4ce4-b142-cc857b0992e3)

### `variables.tf`

![Screenshot (125)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/50118b07-a6fc-41e3-935d-e2fd27cd8ce1)

Finally for the `s3` folder, both files are shown below:

### `main.tf`

![Screenshot (126)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/ccb31271-dc25-441c-bb6a-892ac405c0bb)

### `variables.tf`

![Screenshot (127)](https://github.com/emmanuelkyeremeh/MLOps-project/assets/71068159/b88fdd05-564d-4b40-a731-277efcf47b1a)

