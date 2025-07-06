
# 📂 DVC (Data Version Control) — Quick Commands Cheat Sheet


## 🚀 Initialize DVC

```bash
# Initialize DVC in your project directory
dvc init

```

## 📦 Track Data
```bash
# Add a data file for DVC to track
dvc add data.csv

# Add the .dvc file and .gitignore to Git
git add data.csv.dvc .gitignore
```


## ☁️ Configure Remote Storage
```bash
# Add an S3 bucket (or other remote) and set it as default
dvc remote add -d myremote s3://bucketname
```


## 🔄 Push & Pull Data
```bash
# Push data to remote storage
dvc push

# Pull data from remote storage
dvc pull
```

## 🔁 Reproduce Pipeline
```bash
# Reproduce pipeline steps
dvc repro

# Visualize pipeline DAG (directed acyclic graph)
dvc dag
```


## 🧪 Experiment Tracking

### ✅ Running Experiments

> 📌 **Note:** For advanced experiment tracking, MLflow is often better — but DVC works well too!

```python
from dvclive import Live

# Example usage in your training script
with Live(save_dvc_exp=True) as live:
    live.log_metric("accuracy", metric["Accuracy Score"])
    live.log_metric("precision", metric["Precision Score"])
    live.log_params(param)
```


### ⚡ DVC Experiment Commands
```bash
# Run an experiment
dvc exp run

# Show experiment results in the terminal
dvc exp show

# Remove a specific experiment
dvc exp remove <exp_name>

# Apply (reproduce) a specific experiment
dvc exp apply <exp_name>
```


## ✅ Summary

| Task                    | Command/Notes                                                       |
| ----------------------- | ------------------------------------------------------------------- |
| Init DVC                | `dvc init`                                                          |
| Track data              | `dvc add <file>`                                                    |
| Push/Pull data          | `dvc push` / `dvc pull`                                             |
| Remote storage          | `dvc remote add -d myremote <remote>`                               |
| Reproduce pipeline      | `dvc repro`                                                         |
| Visualize DAG           | `dvc dag`                                                           |
| Run/Manage experiments  | `dvc exp run` / `dvc exp show` / `dvc exp remove` / `dvc exp apply` |
| Log live metrics/params | `dvclive.Live()` context manager                                    |



