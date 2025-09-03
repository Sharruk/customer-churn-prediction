import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("📊 Customer Churn Prediction App")

st.sidebar.header("Enter Customer Information")

def user_input():
    gender = st.sidebar.selectbox("Gender", ["Male","Female"])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0,1])
    Partner = st.sidebar.selectbox("Partner", ["Yes","No"])
    Dependents = st.sidebar.selectbox("Dependents", ["Yes","No"])
    tenure = st.sidebar.number_input("Tenure (months)", 0, 72, 12)
    PhoneService = st.sidebar.selectbox("Phone Service", ["Yes","No"])
    MultipleLines = st.sidebar.selectbox("Multiple Lines", ["Yes","No","No phone service"])
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL","Fiber optic","No"])
    OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes","No","No internet service"])
    OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes","No","No internet service"])
    DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes","No","No internet service"])
    TechSupport = st.sidebar.selectbox("Tech Support", ["Yes","No","No internet service"])
    StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes","No","No internet service"])
    StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes","No","No internet service"])
    Contract = st.sidebar.selectbox("Contract", ["Month-to-month","One year","Two year"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes","No"])
    PaymentMethod = st.sidebar.selectbox(
        "Payment Method", 
        ['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)']
    )
    MonthlyCharges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 500.0)

    # Create DataFrame with ALL required columns
    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }
    return pd.DataFrame(data, index=[0])

# Collect input
input_df = user_input()

# Predict button
if st.button("Predict"):
    try:
        proba = model.predict_proba(input_df)[0,1]
        st.subheader(f"🔮 Churn Probability: {proba:.2%}")
        st.write("Prediction:", "⚠️ Will Churn" if proba > 0.5 else "✅ Will Stay")
    except Exception as e:
        st.error(f"Error: {e}")
