# 📊 MLflow Quick Commands Cheat Sheet



## 🚀 Start MLflow Tracking UI
```bash
# Launch the MLflow UI on localhost:5000 by default
mlflow ui
```





## 📝 Logging Metrics & Parameters
```python
import mlflow

# Start a new MLflow run
with mlflow.start_run():
    # Log a metric
    mlflow.log_metric("Accuracy Score", accuracy)
    
    # Log parameters
    mlflow.log_param("Max Depth", max_depth)
    mlflow.log_param("n_estimators", n_estimators)
```





## 📂 Manage Experiments
```python
# Create or set an active experiment
mlflow.set_experiment("Ml-Flow-2")
```





## 🏷️ Add Tags
```python
# Add custom tags to your run
mlflow.set_tags({
    "Author": "Haseeb",
    "Model": "Random Forest"
})
```





## 📦 Log a Model
```python
import mlflow.sklearn

# Log a trained scikit-learn model
mlflow.sklearn.log_model(
    sk_model=model,
    name="random_forest_model"
)
```





## ⚡ Automatic Logging
```python
# Enable automatic logging for supported libraries (e.g., sklearn, XGBoost)
mlflow.autolog()
```







## 🚀 Example Run
```python
import mlflow
import mlflow.sklearn

mlflow.set_experiment("Ml-Flow-2")

with mlflow.start_run():
    mlflow.set_tags({
        "Author": "Haseeb",
        "Model": "Random Forest"
    })
    
    mlflow.log_metric("Accuracy Score", accuracy)
    mlflow.log_param("Max Depth", max_depth)
    mlflow.log_param("n_estimators", n_estimators)
    
    mlflow.sklearn.log_model(sk_model=model, name="random_forest_model")
```