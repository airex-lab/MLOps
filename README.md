# MLOps
Design for an MLOps pipeline

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
