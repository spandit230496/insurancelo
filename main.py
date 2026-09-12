import streamlit as st
from prediction_helper import predict


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Premium Predictor")
st.write("Enter customer details to predict the annual insurance premium.")

st.divider()


# ---------------------------------------------------------
# Customer Information
# ---------------------------------------------------------

col1, col2 = st.columns(2)


with col1:
    st.subheader("👤 Personal Details")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Married", "Unmarried"]
    )

    number_of_dependants = st.number_input(
        "Number of Dependants",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    region = st.selectbox(
        "Region",
        [
            "Northeast",
            "Northwest",
            "Southeast",
            "Southwest"
        ]
    )

    employment_status = st.selectbox(
        "Employment Status",
        [
            "Salaried",
            "Self-Employed",
            "Unemployed",
            "Retired"
        ]
    )


with col2:
    st.subheader("🏥 Health & Insurance")

    bmi_category = st.selectbox(
        "BMI Category",
        [
            "Underweight",
            "Normal",
            "Overweight",
            "Obesity"
        ]
    )

    smoking_status = st.selectbox(
        "Smoking Status",
        [
            "No Smoking",
            "Occasional",
            "Regular"
        ]
    )

    medical_history = st.selectbox(
        "Medical History",
        [
            "None",
            "Diabetes",
            "Heart Disease",
            "High Blood Pressure",
            "Thyroid"
        ]
    )

    income_level = st.selectbox(
        "Income Level",
        [
            "<10L",
            "10L - 25L",
            "25L - 40L",
            "> 40L"
        ]
    )

    income_lakhs = st.number_input(
        "Income (Lakhs)",
        min_value=0.0,
        max_value=1000.0,
        value=10.0,
        step=0.5
    )

    insurance_plan = st.selectbox(
        "Insurance Plan",
        [
            "Bronze",
            "Silver",
            "Gold"
        ]
    )


st.divider()


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if st.button("🔮 Predict Premium", use_container_width=True):

    input_data = {
        "Age": age,
        "Gender": gender,
        "Region": region,
        "Marital Status": marital_status,
        "Number of Dependants": number_of_dependants,
        "BMI Category": bmi_category,
        "Smoking Status": smoking_status,
        "Employment Status": employment_status,
        "Income Level": income_level,
        "Income in Lakhs": income_lakhs,
        "Medical History": medical_history,
        "Insurance Plan": insurance_plan,

        # Add this if your trained model expects it
        "Genetical Risk": 0
    }

    try:

        prediction = predict(input_data)

        st.success(
            f"### 💰 Estimated Annual Premium: ₹{prediction:,.2f}"
        )

    except Exception as e:

        st.error(f"Prediction failed: {e}")
