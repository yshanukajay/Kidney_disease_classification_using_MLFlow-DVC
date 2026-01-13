# 🩺 Kidney Disease Classification using Deep Learning

This project focuses on building an **end-to-end deep learning pipeline** to classify **kidney disease** from medical data/images using best practices in **MLOps**, including configuration management, modular components, pipelines, and experiment tracking with **DVC**.

---

## 📌 Project Overview

The goal of this project is to:
- Train a deep learning model to classify kidney disease
- Maintain a clean, scalable, and production-ready codebase
- Follow an industry-standard ML workflow
- Enable reproducibility using configuration files and DVC

---

## 🧠 Tech Stack

- **Python**
- **Deep Learning** (TensorFlow / PyTorch)
- **DVC** (Data Version Control)
- **YAML** (Configuration Management)
- **Flask / FastAPI** (for app deployment)
- **Git**

---


## 🔄 Project Workflow

Follow the steps below **in order** to build, train, and deploy the model:

### 1️⃣ Update `config.yaml`
- Define paths for artifacts
- Configure data ingestion and model directories

### 2️⃣ Update `secrets.yaml` *(Optional)*
- Store sensitive information such as:
  - API keys
  - Database credentials
- **Do not push this file to GitHub**

### 3️⃣ Update `params.yaml`
- Define model hyperparameters:
  - Learning rate
  - Batch size
  - Epochs
  - Image size
  - Optimizer settings

### 4️⃣ Update the Entity
- Define dataclasses/entities for:
  - Data ingestion
  - Model training
  - Model evaluation
- Ensures type safety and clean architecture

### 5️⃣ Update Configuration Manager (`src/config`)
- Reads:
  - `config.yaml`
  - `params.yaml`
  - `secrets.yaml`
- Returns structured configuration objects

### 6️⃣ Update Components
Each component handles **one responsibility**:
- Data ingestion
- Data validation
- Model training
- Model evaluation
- Model saving

### 7️⃣ Update the Pipeline
- Orchestrates the execution of components
- Maintains a clean flow of data across stages

### 8️⃣ Update `main.py`
- Entry point for training pipeline
- Executes the full workflow step-by-step

### 9️⃣ Update `dvc.yaml`
- Defines DVC stages:
  - Data ingestion
  - Training
  - Evaluation
- Enables experiment tracking and reproducibility

### 🔟 `app.py`
- Used for **model inference**
- Serves predictions through an API or web interface



