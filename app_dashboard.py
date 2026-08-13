import streamlit as st
import pandas as pd
import joblib
import os

st.title("AttritionX - App Churn Predictor")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your user data CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data)

    # Load model
    if os.path.exists('model/saved_model.pkl'):
        model = joblib.load('model/saved_model.pkl')

        # Prepare features like your training script did
        data['gender'] = data['gender'].apply(lambda x: 1 if x == 'Male' else 0)
        features = data[['gender', 'SeniorCitizen', 'MonthlyCharges']]

        # Predict churn
        predictions = model.predict(features)
        data['Churn_Prediction'] = predictions

        st.write("Prediction Results:")
        st.dataframe(data)

        # Save results to CSV
        data.to_csv("churn_predictions.csv", index=False)
        st.success("Predictions saved to churn_predictions.csv")

    else:
        st.error("Model file not found! Please run training first.")
S