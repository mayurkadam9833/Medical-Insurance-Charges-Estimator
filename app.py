import streamlit as st 
import pandas as pd 
from src.Insurance_Claim_Severity_Prediction.pipeline.prediction import PredictionPipeline


# App title 
st.title("Insurance Claim Severity Estimator")

# Description in Markdown
st.markdown("""
Welcome to the **Insurance Cost Calculator**! 🏥💰  

This app allows you to estimate your insurance charges based on the following inputs:
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region  

Simply enter your details in the sidebar and click **Estimate Insurance Cost** to see your predicted charges.
""")

# user inputs
age=st.sidebar.number_input(label="Age",min_value=1,max_value=100)
sex=st.sidebar.selectbox(label="Sex",options=["female","male"])
bmi=st.sidebar.number_input(label="BMI")
children=st.sidebar.number_input(label="No. of childrens",min_value=0,max_value=10)
smoker=st.sidebar.selectbox(label="smoker",options=["yes","no"])
region=st.sidebar.selectbox(label="region",options=["southeast","southwest","northwest","northeast"])

# button for prediction
if st.button("Estimate Insurance Cost"):
    data=pd.DataFrame({
        "age":[age],
        "sex":[sex],
        "bmi":[bmi],
        "children": [children],
        "smoker":[smoker],
        "region":[region]
    })  # create data frame of input data

    pred=PredictionPipeline()  # create obj of prediction pipeline

    prediction=pred.prediction(data)   # prediction on given data

    st.success(f"💰 Estimated insurance charges:  {prediction[0]:.2f} $") # print prediction value


