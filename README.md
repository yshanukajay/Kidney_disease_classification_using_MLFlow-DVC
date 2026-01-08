# Kidney Disease Classification using MLFlow & DVC

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![DVC](https://img.shields.io/badge/Data-DVC-orange)](https://dvc.org/)
[![MLFlow](https://img.shields.io/badge/Experiments-MLFlow-blueviolet)](https://mlflow.org/)

## 📌 Project Overview
This project focuses on the automated classification of kidney diseases (such as Tumors, Stones, Cysts, or Normal) using Deep Learning. By leveraging **MLflow** and **DVC**, the project ensures full reproducibility, experiment tracking, and efficient data management.

### Key Features
* **Deep Learning Framework:** Built using TensorFlow/Keras for high-accuracy image classification.
* **Data Versioning (DVC):** Tracks large datasets and model weights without bloating the Git repository.
* **Experiment Tracking (MLflow):** Logs parameters, metrics (Accuracy, Loss), and model artifacts for every run.
* **Modular Pipeline:** Clear separation of data ingestion, preprocessing, training, and evaluation for production readiness.

---

## 🏗️ Project Structure
```text
├── config/             # Configuration files (YAML)
├── artifacts/          # Data and model artifacts (tracked by DVC)
├── src/                # Source code
│   ├── components/     # Modular pipeline steps (Data Ingestion, Training, etc.)
│   ├── pipeline/       # Execution pipelines (Training/Prediction)
│   └── constants/      # Constant variables
├── dvc.yaml            # DVC pipeline definition
├── params.yaml         # Hyperparameters for training
├── requirements.txt    # Project dependencies
└── main.py             # Entry point for execution

🚀 Getting Started
1. Environment Setup
Bash

# Clone the repository
git clone [https://github.com/your-username/Kidney_disease_classification_using_MLFlow-DVC.git](https://github.com/your-username/Kidney_disease_classification_using_MLFlow-DVC.git)
cd Kidney_disease_classification_using_MLFlow-DVC

# Create a virtual environment
conda create -n kidney python=3.8 -y
conda activate kidney

# Install dependencies
pip install -r requirements.txt
2. Data Version Control (DVC)
To pull the data and pre-trained weights tracked by DVC:

Bash

dvc pull
3. Running the Pipeline
You can run the entire pipeline (Data Ingestion -> Base Model Creation -> Training -> Evaluation) using DVC:

Bash

dvc repro
📊 MLOps Integration
MLflow Tracking
This project uses MLflow to track experiments. To view the dashboard and compare your training runs:

Bash

mlflow ui
Once the server is running, visit http://localhost:5000 in your browser to analyze metrics and parameters.

Pipeline Visualization
To visualize the project's Directed Acyclic Graph (DAG) and see how data flows through the stages:

Bash

dvc dag
🛠️ Tech Stack
Deep Learning: TensorFlow / Keras

MLOps: MLflow, DVC

Language: Python

Deployment/Environment: Conda, Git
