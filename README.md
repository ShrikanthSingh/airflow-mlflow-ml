# Airflow 2.x for ML Pipeline 

This is the git repo for learning airflow pipeline implementation for machine learning use case. The code has been improvised from the source repositories:
1. e2e-ml-pipeline-airflow - https://github.com/NicoloAlbanese/airflow-ml-pipeline-mvp
2. pycon-sweden-airflow-ml-pipelines - https://github.com/pycon-ml/airflow_workshop

## Pre-requisites

You should have `docker` and `docker-compose` installed on your machine !

The easiest way to have everything ready for the workshop is to install [Docker Desktop](https://docs.docker.com/desktop/.)

### Docker resource requirement
Minimum resource requirement for docker to start all the services is mentioned below:

| Resource    | Recommendation |
| ----------- | -------------- |
| Memory      | 3 GB           |
| CPU         | 2 CPU          |


## Getting started


### 1. Clone this repo

Clone the repo and cd into corresponding folder.

### 2. Use docker-compose to start the applications:

```
docker-compose up
```
### 4. Access services from browser

#### **Airflow**

*UI*: http://localhost:8080

*Username*: airflow

*Password*: airflow

#### **MLflow**

http://localhost:5000

#### **Celery Flower**

http://localhost:5555

## Tear down

Stop and remove containers, networks, images, and volumes

```
docker-compose down
```
## Supplements for troubleshooting

1. https://stackoverflow.com/questions/66172375/docker-desktop-is-using-12-gb-ram-to-run-one-container-with-24-mb-ram
2. https://stackoverflow.com/questions/66699394/airflow-how-to-get-pip-packages-installed-via-their-docker-compose-yml/66701128#66701128
3. https://github.com/helm/charts/issues/23589#issuecomment-878709783

## References

1. https://pretalx.com/pycon-sweden-2021/talk/JRCLRG/
2. https://towardsdatascience.com/end-to-end-machine-learning-pipeline-with-docker-and-apache-airflow-from-scratch-35f6a75f57ad