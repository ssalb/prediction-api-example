# Containerised Flask REST API template for predictive models.

## Overview

This is a template using Docker containers to deploy a pre-trained ML model REST API using nginx, gunicorn, redis and flask. It is composed of four Docker images:

- `api`: running the API using Flask and gunicorn
- `ml_service`: runs the model in a separate instance.
- `redis`: simply working as a messaging bus.
- `nginx`: used as a reversed proxy (and load balancer if needed).

In this way, clients connect to the `nginx` instance, which acts as a proxy and forwards the requests to the `api` instance which puts the request's data into redis. The `ml_service` processes (only one in this case as example, see [replicas](https://docs.docker.com/compose/compose-file/#replicas)) take batches from the queue, run these batches through the model, and place the results back in `redis`. Finally the `api` takes the results, appends them to the API response and removes it.

## How to use

You'll need to implement a few functions at least (see `ml_service/src/model.py`, `api/api.py` and `ml_service/model_process.py`), and perhaps edit the `requirements.txt` files in `api/` and/or `ml_service/`. Additionally, you might want to edit the ports in `docker-compose.yml`, as well as `nginx/nginx_flask.conf`. You can find an example [here](https://github.com/ssalb/prediction-api-example).

Assuming you have docker-compose installed (look here if you don't: https://docs.docker.com/compose/install/) simply run:

```
$ docker-compose build
$ docker-compose up
```

it should be now available under `localhost:5000` (you can modify the port in `docker-compose.yml`).
