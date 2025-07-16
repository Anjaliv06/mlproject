# End to end machine learning project

# 🎓 Student Performance Prediction ML App

An end-to-end machine learning web application that predicts a student's **math score** based on their demographic and academic inputs. Built using **Python**, **Scikit-learn**, and deployed with **Streamlit**.

---

## 🚀 Live Demo

🔗 **Streamlit App**: [Click Here to Try the App](https://mlproject-student-score-prediction.streamlit.app/)

📁 **GitHub Repository**: [https://github.com/YourUsername/student-performance-predictor](https://github.com/Anjaliv06/mlproject)

---

## 🧠 Problem Statement

The goal is to predict a student's math performance based on various input features like:

- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Reading score
- Writing score

---

## 📊 Tech Stack

| Component              | Tools Used                               |
|------------------------|-------------------------------------------|
| ML Model               | Scikit-learn (Linear Regression)          |
| Data Manipulation      | Pandas, NumPy                            |
| Frontend UI            | Streamlit                                |
| Model Deployment       | Streamlit Cloud                          |
| Serialization          | Joblib (`model.pkl`)                     |
| Project Structure      | Modular ML Pipeline with OOP & Logging   |

---

## 🏗️ Project Structure

student-performance-predictor/
│
├── streamlit_app.py # Main Streamlit frontend
├── requirements.txt # Dependencies
├── artifacts/
│ └── model.pkl # Trained ML model
│
├── notebook/
│ └── data/
│ └── raw.csv # Input dataset
│
└── src/
├── pipeline/
│ ├── predict_pipeline.py # Loads model, handles predictions
│ └── custom_data.py # Converts form input to DataFrame
├── components/
│ └── data_ingestion.py # Reads, splits, and saves data
├── logger.py # Logging setup
└── exception.py # Custom exception handling

## 🧪 How to Run Locally

### 🔧 Setup

```bash
# Clone the repository
git clone https://github.com/Anjaliv06/mlproject
cd student-performance-predictor

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

## Run the Streamlit app
streamlit run streamlit_app.py

