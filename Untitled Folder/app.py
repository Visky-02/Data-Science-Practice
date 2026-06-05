import streamlit as st
import pickle

st.set_page_config(page_title="Titanic Predictor", layout="wide")

st.title("🚢 Titanic Survival Predictor")
st.subheader("Kya tu Titanic par zinda bachta?")

try:
    model = pickle.load(open('titanic_gbc_model.pkl', 'rb'))
    st.success("✅ Model Load Hogya CEO!")
except:
    st.error("⚠️ Model file nahi mili!")

st.write("---")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.radio("Gender", ["Male", "Female"])
age = st.slider("Age", 0, 100, 25)

if st.button("Predict"):
    st.balloons()
    st.write("UI aur Model link successful! Backend logic next session mein detail mein samjhenge.")