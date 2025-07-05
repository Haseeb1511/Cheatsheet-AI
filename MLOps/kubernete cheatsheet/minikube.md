
---
# 🚢 Kubernetes & Minikube Quick Commands
````markdown

## 📦 What is Kubernetes?

> **Kubernetes** is a system that helps run, manage, and scale apps automatically — like a smart manager for your app’s servers.

---

## 🚀 Start Minikube Cluster

```bash
# Start Minikube using Docker as the driver
minikube start --driver=docker

# Create a second cluster running an older Kubernetes version
minikube start -p aged --kubernetes-version=v1.16.1

# Start Minikube with default settings
minikube start

# Start Minikube with 2 nodes (default is 1 Control Plane)
minikube start --nodes=2
````

---

## 🔍 Get Nodes & Pods

```bash
# Get all nodes
kubectl get nodes -A

# Get all running pods (short)
kubectl get po -A

# Get all running pods (default namespace)
kubectl get pods

# Using Minikube’s built-in kubectl
minikube kubectl -- get po -A
```

---

## 📊 Minikube Dashboard & Cluster Control

```bash
# Open Minikube Dashboard
minikube dashboard

# Pause Minikube cluster
minikube pause

# Unpause Minikube cluster
minikube unpause

# Stop Minikube cluster
minikube stop
```

---

## 🗂️ Manage Images

```bash
# List images in Minikube
minikube image list

# Load local Docker image into Minikube
minikube image load <docker_image_name>
```

---

## ⚙️ Deploy Applications

```bash
# Apply deployment YAML
kubectl apply -f <deployment.yaml>

# Expose and access the deployed app
minikube service <app_name_in_yaml>
```

---

## 🧹 Clean Up Resources

```bash
# Delete a specific pod
kubectl delete pod <pod_name>

# Delete a specific deployment
kubectl delete deployment <deployment_name>

# Delete all Minikube clusters
minikube delete --all
```

---

## 🔍 Other Useful Commands

```bash
# Get endpoints
kubectl get endpoints

# Get pods
kubectl get pods

# View pod logs in real-time
kubectl logs -f <pod_name>
```

---

## ✅ Recommended Quick Flow

```bash
# Start Minikube
minikube start

# List images
minikube image list

# Load Docker image into Minikube
minikube image load <docker_image_name>

# Apply deployment file
kubectl apply -f <deployment.yaml>

# Run the deployed app
minikube service <app_name_in_yaml>
```

---


```

---
