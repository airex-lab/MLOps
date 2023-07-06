# MLOps
Design for an MLOps pipeline

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

# Containerization using Docker

- Build an image
``` shell
docker build -t mlops-api .
```

- Bulid a container (run the image)
``` shell
docker run -p 8000:8000 mlops-api.
```

# Orchestration and Containerization with Kubernetes and Docker

`minikube` is being used to run `kubernetes` run on a single cluster for development purposes

## Setting up
- Initialize `minikube` to make create an environment for `kubernetes`
``` shell
minikube start
```
- List the docker images inside `minikube`
``` shell
minikube image list
```

- Add the docker image inside the minikube VM
``` shell
eval $(minikube docker-env)
docker build -t mlops-api .
```

- Create a deployment(container) in kubernetes
``` shell
kubectl create deployment mlops-deploy --image=mlops-api
```

- Check if it's running properly
``` shell
kubectl get deployment
kubectl get pod
```

- Expose the deployment
``` shell
kubectl expose deployment mlops-deploy --type=NodePort --port=8000
```

- Check Node Port
``` shell
kubectl get svc
```

- Run the service tunnel
``` shell
minikube service mlops-deploy
```

- After this the api can be accessed

## Tips

- Manually increase the replicas(number of containers)
``` shell
kubectl scale deploy/mlops-deploy --replicas=5
```

- View logs of a particular container

``` shell
kubectl logs -f <container-name>
```

# References
- [Deploy ML models on Kubernetes video](https://youtu.be/DQRNt8Diyw4)
- [Accessing Apps in Minikube](https://minikube.sigs.k8s.io/docs/handbook/accessing/)
- [FastApi in Containers](https://fastapi.tiangolo.com/deployment/docker/)

# Further Reading
- [Kubernetes](https://kubernetes.io/docs/home/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [FastApi](https://pypi.org/project/fastapi/)

# TODO
- Use cookiecutter/yeoman for project structure
- Add unit tests
- Add github actions for running the unit tests on pull requests
- Use dvc to manage data versions
- Use mlflow/kubeflow for mlops
