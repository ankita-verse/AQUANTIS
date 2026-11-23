import streamlit as st
import pandas as pd
import joblib

# Load the trained Decision Tree model
model = joblib.load("results/decision_tree_model.pkl")

# Application title
st.title("AquaSense: Smart Water Quality Prediction")

st.write(
    "An educational machine learning application "
    "that predicts water potability using water quality parameters."
)

st.subheader("Enter Water Quality Parameters")


# Input fields
ph = st.number_input("pH", value=7.0)
Hardness = st.number_input("Hardness", value=200.0)
Solids = st.number_input("Solids", value=20000.0)
Chloramines = st.number_input("Chloramines", value=7.0)
Sulfate = st.number_input("Sulfate", value=300.0)
Conductivity = st.number_input("Conductivity", value=400.0)
Organic_carbon = st.number_input("Organic Carbon", value=10.0)
Trihalomethanes = st.number_input("Trihalomethanes", value=60.0)
Turbidity = st.number_input("Turbidity", value=4.0)

# Prediction button
if st.button("Predict Water Potability"):

    input_data = pd.DataFrame([[
        ph,
        Hardness,
        Solids,
        Chloramines,
        Sulfate,
        Conductivity,
        Organic_carbon,
        Trihalomethanes,
        Turbidity
    ]], columns=[
        "ph",
        "Hardness",
        "Solids",
        "Chloramines",
        "Sulfate",
        "Conductivity",
        "Organic_carbon",
        "Trihalomethanes",
        "Turbidity"
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("The model predicts: POTABLE")
    else:
        st.warning("The model predicts: NON-POTABLE")

# Important disclaimer
st.info(
    "Educational dataset prediction only. "
    "This is not a certified water-safety test. "
    "Do not use this prediction to decide whether water is safe to drink."
)
