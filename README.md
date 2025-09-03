# 📊 Customer Churn Prediction  

A Machine Learning project to predict customer churn in a telecom company.  
The app is built using **Scikit-learn**, **Streamlit**, and **Pandas**.  

---

## 📝 Problem Statement  

Customer churn (when customers stop using a service) is a major business problem.  
The goal is to **predict whether a customer will churn (Yes/No)** based on their demographics, account information, and service usage.  

---

## 📂 Project Structure  
```bash
customer-churn-prediction/
│
├── data/
│   └── churn.csv                # Dataset (Telco Customer Churn)
├── churn_prediction.ipynb       # Model training notebook
├── model.pkl                    # Saved trained model
├── app.py                       # Streamlit web app
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                   # 

```

Installation

Clone this repo:
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```
▶️ Run the App

Start the Streamlit app with:
```bash
streamlit run app.py
```

Then open http://localhost:8501
 in your browser.
📊 Features

Interactive form to input customer details (via sidebar)

Predicts churn probability (0–100%)

Displays final prediction:

✅ Will Stay

⚠️ Will Churn

Powered by ML model trained on telecom dataset

📈 Model Training

Dataset: Telco Customer Churn Dataset (Kaggle)

Preprocessing: Missing value handling, categorical encoding, feature scaling

Balancing: SMOTE applied to handle class imbalance

Algorithms Tested: Logistic Regression, Random Forest, Gradient Boosting

Final Model: Saved as model.pkl


📊 Model Evaluation & Comparison
🔎 Model Performance Overview
Model	Accuracy	ROC AUC
Logistic Regression	0.737	0.840
Random Forest	0.776	0.818
XGBoost	0.786	0.826
📌 Logistic Regression
              precision    recall  f1-score   support

           0       0.91      0.71      0.80      1035
           1       0.50      0.80      0.62       374

    accuracy                           0.74      1409
   macro avg       0.70      0.76      0.71      1409
weighted avg       0.80      0.74      0.75      1409


ROC AUC: 0.8397

📌 Random Forest
              precision    recall  f1-score   support

           0       0.85      0.85      0.85      1035
           1       0.58      0.57      0.57       374

    accuracy                           0.78      1409
   macro avg       0.71      0.71      0.71      1409
weighted avg       0.77      0.78      0.78      1409


ROC AUC: 0.8179

📌 XGBoost
              precision    recall  f1-score   support

           0       0.86      0.85      0.85      1035
           1       0.59      0.61      0.60       374

    accuracy                           0.79      1409
   macro avg       0.73      0.73      0.73      1409
weighted avg       0.79      0.79      0.79      1409


ROC AUC: 0.8262
Example Prediction

Input:

Gender: Male

Senior Citizen: 1

Partner: Yes

Dependents: Yes

Tenure: 12 months

Contract: Month-to-month

Monthly Charges: 70.0

Total Charges: 500.0

Output:

🔮 Churn Probability: 7.48%
✅ Will Stay




# 📊 Customer Churn Prediction  

A Machine Learning project to predict **customer churn** in a telecom company.  
The app is built using **Scikit-learn**, **Streamlit**, and **Pandas**.  

---

## 📝 Problem Statement  

Customer churn (when customers stop using a service) is a major business challenge.  
The goal of this project is to **predict whether a customer will churn (Yes/No)** based on their demographics, account information, and service usage.  

---

## 📂 Project Structure  

customer-churn-prediction/
│
├── data/
│ └── churn.csv # Dataset (Telco Customer Churn)
├── churn_prediction.ipynb # Model training notebook
├── model.pkl # Saved trained model
├── app.py # Streamlit web app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignore unnecessary files

yaml
Copy code

---

## ⚙️ Installation  

Clone this repo:  
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
Create virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Run the App
Start the Streamlit app with:

bash
Copy code
streamlit run app.py
Then open http://localhost:8501 in your browser.

📊 Features
Interactive form to input customer details (via sidebar)

Predicts churn probability (0–100%)

Displays final prediction:

✅ Will Stay

⚠️ Will Churn

Powered by ML model trained on telecom dataset

📈 Model Training
Dataset: Telco Customer Churn Dataset (Kaggle)

Preprocessing: Missing value handling, categorical encoding, feature scaling

Balancing: SMOTE applied to handle class imbalance

Algorithms Tested: Logistic Regression, Random Forest, Gradient Boosting

Final Model: Saved as model.pkl

📊 Model Evaluation & Comparison
🔎 Model Performance Overview
Model	Accuracy	ROC AUC
Logistic Regression	0.737	0.840
Random Forest	0.776	0.818
XGBoost	0.786	0.826

📌 Logistic Regression
yaml
Copy code
              precision    recall  f1-score   support

           0       0.91      0.71      0.80      1035
           1       0.50      0.80      0.62       374

    accuracy                           0.74      1409
   macro avg       0.70      0.76      0.71      1409
weighted avg       0.80      0.74      0.75      1409
ROC AUC: 0.8397

📌 Random Forest
yaml
Copy code
              precision    recall  f1-score   support

           0       0.85      0.85      0.85      1035
           1       0.58      0.57      0.57       374

    accuracy                           0.78      1409
   macro avg       0.71      0.71      0.71      1409
weighted avg       0.77      0.78      0.78      1409
ROC AUC: 0.8179

📌 XGBoost
yaml
Copy code
              precision    recall  f1-score   support

           0       0.86      0.85      0.85      1035
           1       0.59      0.61      0.60       374

    accuracy                           0.79      1409
   macro avg       0.73      0.73      0.73      1409
weighted avg       0.79      0.79      0.79      1409
ROC AUC: 0.8262

⚠️ Note: The warning regarding use_label_encoder in XGBoost is a known deprecation and does not affect model performance.

🔮 Example Prediction
Input:

Gender: Male

Senior Citizen: 1

Partner: Yes

Dependents: Yes

Tenure: 12 months

Contract: Month-to-month

Monthly Charges: 70.0

Total Charges: 500.0

Output:

yaml
Copy code
Churn Probability: 7.48%
✅ Will Stay
✅ Final Model Selection
After evaluating multiple algorithms, XGBoost showed the best balance of accuracy and ROC AUC.
Hence, the final trained model was saved as model.pkl for deployment.

yaml
Copy code

---

Do you want me to also make a **badge section** (e.g., Python, Streamlit, Scikit-learn, Kaggle dataset) at the top for a more professional look?







Ask ChatGPT
