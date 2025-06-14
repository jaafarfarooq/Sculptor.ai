import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://localhost:8000/TDEE/"

# App layout
st.set_page_config(page_title="TDEE Calculator", layout="centered")
st.title("🧮 Total Daily Energy Expenditure (TDEE) Calculator")
st.markdown("Estimate your daily calorie needs and macronutrient breakdown based on your profile.")

# User input form
with st.form("tdee_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        height = st.number_input("Height (cm)", min_value=50.0, step=0.1)
        weight = st.number_input("Weight (kg)", min_value=20.0, step=0.1)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
        activity = st.selectbox("Activity Level", ["sedentary", "light", "moderate", "heavy", "athlete"])
        goal = st.selectbox("Goal", ["cut", "maintain", "bulk"])

    submitted = st.form_submit_button("Calculate TDEE")

# When form is submitted
if submitted:
    payload = {
        "age": age,
        "height_cm": height,
        "weight_kg": weight,
        "gender": gender.lower(),
        "activity_level": activity,
        "goal": goal
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success("Results:")
            col1, col2, col3 = st.columns(3)
            col1.metric("TDEE", f"{result['TDEE']} kcal")
            col2.metric("Adjusted Calories", f"{result['Adjusted Calories']} kcal")
            st.divider()
            col1.metric("Protein", f"{result['Protein (g)']} g")
            col2.metric("Carbs", f"{result['Carbs (g)']} g")
            col3.metric("Fats", f"{result['Fats (g)']} g")
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Connection failed: {e}")
