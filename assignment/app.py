import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained Logistic Regression model and StandardScaler
with open('titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('titanic_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Configure the Streamlit application title and description
st.title("🚢 Titanic Survival Prediction App")
st.write("Logistic Regression Model Deployment - ExcelR Project")

# Define user input fields for the prediction parameters
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.radio("Gender", ["Male", "Female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Ticket Fare ($)", 0.0, 500.0, 30.0)
embarked = st.selectbox("Port of Embarkation", ["C (Cherbourg)", "Q (Queenstown)", "S (Southampton)"])

# Preprocess categorical inputs to match the training data format (Dummy encoding)
sex_male = 1 if sex == "Male" else 0
embarked_q = 1 if embarked == "Q (Queenstown)" else 0
embarked_s = 1 if embarked == "S (Southampton)" else 0

# Execute prediction logic upon button click
if st.button("Predict Survival"):
    
    # Construct a DataFrame from the user inputs
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Sex_male': [sex_male],
        'Embarked_Q': [embarked_q],
        'Embarked_S': [embarked_s]
    })

    # Apply standard scaling to the input data
    scaled_input = scaler.transform(input_data)

    # Generate prediction and prediction probability
    prediction = model.predict(scaled_input)
    probability = model.predict_proba(scaled_input)[0][1]

    # Display the final prediction result to the user
    if prediction[0] == 1:
        st.success(f"Prediction: Passenger Survives! 🛟 (Probability: {probability:.2f})")
    else:
        st.error(f"Prediction: Passenger Does Not Survive. ☠️ (Probability: {probability:.2f})")