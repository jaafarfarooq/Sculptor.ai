import streamlit as st
import requests
import pandas as pd

# API URLs
API_BASE = "http://localhost:8000"
TDEE_API = f"{API_BASE}/api/v1/tdee"
SIGNUP_API = f"{API_BASE}/auth/signup"
LOGIN_API = f"{API_BASE}/auth/login"

# Set up page
st.set_page_config(page_title="Sculptor.ai Dashboard", layout="wide")

# Session State Initialization
if "access_token" not in st.session_state:
    st.session_state.access_token = None
if "username" not in st.session_state:
    st.session_state.username = None

# --------------------------
# Sidebar: Authentication
# --------------------------
with st.sidebar:
    st.title("🔐 User Panel")
    auth_action = st.radio("Action", ["Login", "Sign Up"], horizontal=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    auth_submit = st.button(auth_action)

    if auth_submit and username and password:
        payload = {"username": username, "password": password}
        try:
            if auth_action == "Sign Up":
                res = requests.post(SIGNUP_API, params=payload)
                if res.status_code == 200:
                    st.success("✅ Registered! Now log in.")
                else:
                    st.error(f"❌ {res.text}")
            else:
                res = requests.post(LOGIN_API, params=payload)
                if res.status_code == 200:
                    st.session_state.access_token = res.json()["access_token"]
                    st.session_state.username = username
                    st.success("🔓 Logged in!")
                else:
                    st.error("❌ Invalid credentials")
        except Exception as e:
            st.error(f"Connection error: {e}")

    if st.session_state.access_token:
        if st.button("🚪 Logout"):
            st.session_state.access_token = None
            st.session_state.username = None
            st.rerun()

# --------------------------
# Main Dashboard Navigation
# --------------------------
st.title("📊 Sculptor.ai Dashboard")

if st.session_state.access_token:
    menu = st.selectbox("📂 Navigation", ["Home", "TDEE Calculator", "Calorie Tracker", "Food Diary", "Profile"])

    if menu == "Home":
        st.subheader(f"Welcome, {st.session_state.username} 👋")
        st.write("Use the menu above to navigate the dashboard.")
        st.info("More modules coming soon: Meal Planning, Progress Tracking, Analytics...")

    elif menu == "TDEE Calculator":
        st.subheader("🧮 Total Daily Energy Expenditure (TDEE) Calculator")

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

        if submitted:
            payload = {
                "age": age,
                "height_cm": height,
                "weight_kg": weight,
                "gender": gender.lower(),
                "activity_level": activity,
                "goal": goal
            }

            headers = {"Authorization": f"Bearer {st.session_state.access_token}"}

            try:
                response = requests.post(TDEE_API, json=payload, headers=headers)
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

    
    elif menu == "Calorie Tracker":
        st.subheader("🍽️ Calorie & Macronutrient Tracker")
        st.markdown("Enter a food item (e.g., `1 egg`, `2 bananas`, `1 cup rice`) to get its nutritional information.")

        food_input = st.text_input("Enter food item")

        if st.button("Get Nutrition Info") and food_input:
            try:
                from nutritionx import get_nutrition
                result = get_nutrition(food_input)
                if isinstance(result, dict):
                    st.success("Nutrition Facts:")
                    st.metric("Calories", f"{result.get('nf_calories', 'N/A')} kcal")
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Protein", f"{result.get('nf_protein', 'N/A')} g")
                    col2.metric("Carbs", f"{result.get('nf_total_carbohydrate', 'N/A')} g")
                    col3.metric("Fats", f"{result.get('nf_total_fat', 'N/A')} g")

                    with st.expander("🔍 Full Nutrition Details"):
                        st.json(result)
                else:
                    st.error("❌ Failed to fetch nutrition info.")
            except Exception as e:
                st.error(f"Error: {e}")

    elif menu == "Food Diary":
        st.subheader("📝 Food Diary")
        st.markdown("Enter a food item (e.g., `1 egg`, `2 bananas`, `1 cup rice`) to get its nutritional information.")

        # Always check or initialize session state first
        if "food_log" not in st.session_state:
            st.session_state.food_log = []

        food_input = st.text_input("Enter food item")

        if st.button("Log food") and food_input:
            try:
                from nutritionx import get_nutrition
                result = get_nutrition(food_input)
                if isinstance(result, dict):
                    st.session_state.food_log.append({
                        "Food": food_input,
                        "Calories": result.get('nf_calories', 0),
                        "Protein (g)": result.get('nf_protein', 0),
                        "Carbs (g)": result.get('nf_total_carbohydrate', 0),
                        "Fats (g)": result.get('nf_total_fat', 0)
                    })
            except Exception as e:
                st.error(f"Error: {e}")

        # Always show the current log and totals (even if no new entry)
        if st.session_state.food_log:
            st.markdown("### 📋 Logged Foods")
            st.dataframe(st.session_state.food_log)

            # Totals
            df = pd.DataFrame(st.session_state.food_log)
            totals = df[["Calories", "Protein (g)", "Carbs (g)", "Fats (g)"]].sum()
            st.markdown("### 📊 Totals for Today")
            st.write(totals.to_frame().T)
      

    elif menu == "Profile":
        st.subheader("🧾 Profile Overview")
        st.markdown(f"- **Username:** `{st.session_state.username}`")
        #st.markdown(f"- **Access Token:** `{st.session_state.access_token[:25]}...`")

else:
    st.warning("🔒 Please login from the sidebar to access the dashboard.")

