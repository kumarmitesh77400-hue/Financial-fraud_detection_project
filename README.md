# 🛑 Pre-Authorization Financial Fraud Prevention Engine

[![Python Version](https://img.shields.io/badge/Python-3.14%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-XGBoost%20%7C%20SMOTE-orange?logo=scikitlearn&logoColor=white)](https://xgboost.readthedocs.io/)
[![Dashboard Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Security Level](https://img.shields.io/badge/Security-Enterprise%20Pre--Auth-red)](#)

An advanced, real-time machine learning firewall engine designed to intercept and evaluate credit card transaction payloads **before payment authorization**. Built on an optimized **XGBoost Classifier** combined with synthetic oversampling (**SMOTE**) to tackle extreme class imbalances, this system stops fraud *before* capital leaves the account.

---

## 🚀 Core Features

* **Pre-Authorization Interception:** Simulates live gateway overrides that block threats *prior* to clearinghouse settlement.
* **Hybrid Defense Architecture:** Merges a high-speed deterministic rule engine (blocking brute-force CVV attacks & excessive velocity) with deep ML predictive inference.
* **Seamless UI Translation Layer:** Abstracts anonymous Principal Component variables (`V1` to `V28`) into intuitive, human-readable enterprise security telemetry (Location risk, device logs, behavioral profiles).
* **Robust Imbalance Handling:** Trains efficiently on highly skewed data (0.17% fraud ratio) utilizing SMOTE to avoid predictive bias.

---

## 🛠️ Technology Stack

* **Language:** Python 3.14+
* **Frameworks & Libraries:** * `XGBoost` (Gradient Boosted Decision Trees)
  * `Imbalanced-Learn` (SMOTE implementation)
  * `Scikit-Learn` (Feature Scaling & Matrix Evaluations)
  * `Pandas` & `NumPy` (Data Engineering Pipeline)
* **Frontend Dashboard:** `Streamlit`

---

## 📂 Project Architecture

```text
fraud_detection_project/
│
├── data/
│   └── creditcard.csv          # Kaggle Fraud Dataset
│
├── models/
│   ├── scaler.pkl              # Fitted StandardScaler artifact
│   └── xgboost_model.pkl       # Trained XGBoost model artifact
│
├── notebooks/
│   └── training.ipynb          # Jupyter Pipeline (Oversampling -> Model Training)
│
├── app.py                      # Main Streamlit Dashboard Application
├── requirements.txt            # System dependencies
└── README.md                   # Project documentation
