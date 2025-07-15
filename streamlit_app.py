import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Exam Score Predictor", layout="centered")

st.title("📊 Student Performance Prediction")
st.write("Fill the form below to predict **Math score** based on other details.")

# Input fields
gender = st.selectbox("Gender", options=["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", options=[
    "group A", "group B", "group C", "group D", "group E"
])
parental_level_of_education = st.selectbox("Parental Level of Education", options=[
    "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch Type", options=["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", options=["none", "completed"])
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

if st.button("Predict Math Score"):
    # Create CustomData object
    input_data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    df = input_data.get_data_as_data_frame()
    st.subheader("📄 Input Data")
    st.write(df)

    # Prediction
    pipeline = PredictPipeline()
    result = pipeline.predict(df)

    st.success(f"🎯 Predicted Math Score: **{result[0]:.2f}**")

