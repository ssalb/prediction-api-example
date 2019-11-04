# Containerised Flask REST API template for predictive models - An example.

## Overview

This is an example (based on [this template](https://github.com/ssalb/prediction-api-template)) using Docker containers to deploy a pre-trained ML model REST API using nginx, gunicorn, redis and flask. It is composed of four Docker images:

- `api`: running the API using Flask and gunicorn
- `ml_service`: runs the model in a separate instance.
- `redis`: simply working as a messaging bus.
- `nginx`: used as a reversed proxy (and load balancer if needed).

In this way, clients connect to the `nginx` instance, which acts as a proxy and forwards the requests to the `api` instance which puts the request's data into redis. The `ml_service` processes (only one in this case as example, see [replicas](https://docs.docker.com/compose/compose-file/#replicas)) take batches from the queue, run these batches through the model, and place the results back in `redis`. Finally the `api` takes the results, appends them to the API response and removes it.

## How to use

In the [notebooks](../master/notebooks) you can find two jupyter notebooks: `train-my-model.ipynb` and `test-api.ipynb`. The first one trains a Support Vector Classifier (SVC) using the [Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) from scikit-learn and stores the model under `ml_service/model/my-model.pkl`. This model is then used by `ml_service` to make predictions.

After this model is trained, and assuming you have docker-compose installed (look here if you don't: https://docs.docker.com/compose/install/) simply run:

```
$ docker-compose build
$ docker-compose up
```

The predictions api should now be available under `localhost:5000` (you can modify the port in `docker-compose.yml`). Now you can use the second notebook `test-api.ipynb` to make requests to the api, which will respond with the predictions.
