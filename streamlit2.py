import streamlit as st
import pandas as pd
import joblib

#Step4:

model = joblib.load("bank_model.pkl")


st.title(" Financial Inclusion Predictor")
st.write("Predict if a person is likely to have a bank account.")

with st.form("prediction_form"):
    country = st.selectbox("Country", ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
    location = st.selectbox("Location Type", ['Urban', 'Rural'])
    gender = st.selectbox("Gender", ['Female', 'Male'])
    age = st.slider("Age", 16, 100, 30)
    education = st.selectbox("Level of Education", [
        'No formal education', 'Primary education', 'Secondary education',
        'Vocational/Specialised training', 'Tertiary education', 'Other'
    ])
    job_type = st.selectbox("Job Type", [
        'Self employed', 'Government Dependent', 'Formally employed Private',
        'Formally employed Government', 'Informally employed', 'Farming and Fishing',
        'Remittance Dependent', 'No Income', 'Other Income'
    ])

    submit = st.form_submit_button("Predict")

if submit:
    input_data = pd.DataFrame([{
        'country': country,
        'location_type': location,
        'gender_of_respondent': gender,
        'age_of_respondent': age,
        'education_level': education,
        'job_type': job_type
    }])

input_encoded = input_data.copy()
for col in input_encoded.columns:
        input_encoded[col] = input_encoded[col].astype('category').cat.codes

prediction = model.predict(input_encoded)[0]  
result = " has a bank account" if prediction == 1 else "has not a bank account"
st.subheader(result)      