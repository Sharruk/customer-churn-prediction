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
└── report.pdf                   # Detailed project report

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

Input customer details via sidebar form

Predict churn probability (0–100%)

Display prediction: ✅ Will Stay / ⚠️ Will Churn

Uses trained ML model (RandomForest / LogisticRegression based)

📈 Model Training

Dataset: Telco Customer Churn Dataset (Kaggle)

Preprocessing: Missing value handling, categorical encoding, scaling

Balancing: SMOTE applied for imbalanced data

Algorithms tried: Logistic Regression, Random Forest, Gradient Boosting

Final model saved as model.pkl


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
