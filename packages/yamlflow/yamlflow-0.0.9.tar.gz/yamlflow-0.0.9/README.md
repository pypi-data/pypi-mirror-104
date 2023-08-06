# yamlflow
Yet Another ML flow

We follow `convention over configuration` (also known as coding by convention) software design paradigm.

Here are some of the features the `yamlflow` provides.


1. Build and publish your ML solution as a RESTful Web Service `with yaml`.
    
    + You don't need to write web realated code, or dockerfiles.
    
    + You don't need to benchmark which python web server or framework is best in terms of performance.
    
    + WE do it for you. All the best, packed in.


## Metrics for inference

+ Throughput
 (How many requests can server process in some interval of time)

+ Latency
 (How long does it take to get a prediction for a single request)

## Python REST API

```
async
    - web-server(ASGI): Uvicorn, Hypercorn, Daphne
    - web-(micro)framework: Starlete, ...
    - API-framework: FastAPI, ...

sync
    - web-server(WSGI): gunicorn, uWSGI, Gevent, Twisted Web
    - web-(micro)framework: Flask
    - API-framework: None
```


### Project structure 
```
.
├── model
│   ├── ...
│   ├── pipeline.py
│   └── requirements.txt
├── service
│   ├── objects
│   ├── config.py
│   └── predictor.py
├── train
│   ├── ...
│   ├── train.py
│   └── requirements.txt
├── README.md
└── yamlflow.yaml
```

#### example `yamlflow.yaml`
```yaml
kind: Service
meta:
  registry: your.docker.registry
  user: dockerusername
project:
  name: ml-project
  version: 0.1.0
backend:
  runtime: torch
  device: cpu
port: 8002
```

### Installation guide
```bash
pip install yamlflow
```

### User guide
```bash
yamlflow init
yamlflow build
yamlflow run
```

### Developer guide
```
pyenv install 3.8.6
poetry env use ~/.pyenv/versions/3.8.6/bin/python
poetry shell
poetry install
```
