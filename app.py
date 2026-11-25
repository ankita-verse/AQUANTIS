import streamlit as st
import pandas as pd
import joblib
import os
import textwrap

# Page configuration
st.set_page_config(
    page_title="AQUANTIS | Water Quality Predictor Intelligence",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the trained SVM model
model = joblib.load("results/svm_model.pkl")

# Deep Ocean theme
st.markdown("""
<style>

.stApp {
    background-color: #071B2B;
    color: #F1FAFC;
}

[data-testid="stSidebar"] {
    background-color: #102C40;
}

h1, h2, h3 {
    color: #48CAE4;
}

p, label, span {
    color: #F1FAFC;
}

.stButton > button {
    background-color: #168AAD;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 22px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #48CAE4;
    color: #071B2B;
}

</style>
""", unsafe_allow_html=True)

# Sidebar navigation

st.sidebar.title("🌊 AQUANTIS")

st.sidebar.caption("Smart Water Quality Predictor Intelligence")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Water Prediction",
        "Data Insights",
        "Model Performance",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Powered by Machine Learning | SVM Model"
)

# HOME PAGE

if page == "Home":

    st.html("""
    <div style="
        background: linear-gradient(120deg, #102C40, #07516B);
        padding: 45px 35px;
        border-radius: 20px;
        border: 1px solid #168AAD;
        margin-bottom: 30px;
    ">

        <p style="
            color: #48CAE4;
            font-size: 14px;
            letter-spacing: 3px;
            font-weight: bold;
        ">
            INTELLIGENT WATER QUALITY ANALYSIS
        </p>

        <h1 style="
            color: #F1FAFC;
            font-size: 48px;
            margin-bottom: 5px;
        ">
            AQUANTIS
        </h1>

        <h3 style="
            color: #A9C4D0;
            font-weight: 400;
        ">
            Where Water Science Meets Machine Learning
        </h3>

        <p style="
            color: #D5E8EF;
            font-size: 17px;
            line-height: 1.7;
            margin-top: 20px;
        ">
            Exploring water quality through intelligent data
            analysis and predictive machine learning models.
        </p>

    </div>
    """)

    st.markdown("## Explore the Platform")

    st.markdown(
        "Discover the different capabilities of AQUANTIS."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div style="
            background: #102C40;
            padding: 22px;
            border-radius: 15px;
            border: 1px solid #168AAD;
            min-height: 190px;
        ">
            <h2 style="color:#48CAE4;">01</h2>
            <h3 style="color:#F1FAFC;">Water Prediction</h3>
            <p style="color:#A9C4D0;">
                Explore water quality predictions
                using our trained SVM model.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div style="
            background: #102C40;
            padding: 22px;
            border-radius: 15px;
            border: 1px solid #168AAD;
            min-height: 190px;
        ">
            <h2 style="color:#48CAE4;">02</h2>
            <h3 style="color:#F1FAFC;">Data Insights</h3>
            <p style="color:#A9C4D0;">
                Discover patterns and relationships
                through exploratory data analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div style="
            background: #102C40;
            padding: 22px;
            border-radius: 15px;
            border: 1px solid #168AAD;
            min-height: 190px;
        ">
            <h2 style="color:#48CAE4;">03</h2>
            <h3 style="color:#F1FAFC;">Model Performance</h3>
            <p style="color:#A9C4D0;">
                Compare four machine learning
                algorithms and their evaluation metrics.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## Project at a Glance")

    m1, m2, m3 = st.columns(3)

    m1.metric("Water Samples", "3,276")
    m2.metric("Input Parameters", "9")
    m3.metric("ML Algorithms", "4")

    st.markdown("---")

    st.markdown("""
    <div style="
        background: #102C40;
        padding: 18px;
        border-radius: 12px;
        border-left: 4px solid #48CAE4;
    ">
        <h4 style="color:#48CAE4;">
            Research Note
        </h4>
        <p style="color:#D5E8EF;">
            AQUANTIS is an educational machine learning
            project. Its predictions are not certified
            water-safety assessments and must not be used
            alone to determine whether water is safe to drink.
        </p>
    </div>
    """, unsafe_allow_html=True)


# WATER PREDICTION PAGE

elif page == "Water Prediction":

    st.html("""
    <div style="
        background: linear-gradient(120deg, #102C40, #07516B);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #168AAD;
        margin-bottom: 25px;
    ">
        <p style="color:#48CAE4; letter-spacing:2px;">
            AQUANTIS | SVM ANALYSIS
        </p>
        <h1 style="color:#F1FAFC;">
            Water Quality Prediction
        </h1>
        <p style="color:#D5E8EF; font-size:16px;">
            Enter the water quality parameters to explore
            a machine learning-based potability prediction.
        </p>
    </div>
    """)

    st.markdown("### 🔬 Water Sample Parameters")

    st.write(
        "Provide the nine measurements below to analyse "
        "your water sample using our trained SVM model."
    )

    with st.form("water_prediction_form"):

        col1, col2 = st.columns(2)

        with col1:

            ph = st.number_input("pH Level", value=7.0)

            hardness = st.number_input(
                "Hardness", value=200.0
            )

            solids = st.number_input(
                "Total Dissolved Solids", value=20000.0
            )

            chloramines = st.number_input(
                "Chloramines", value=7.0
            )

            sulfate = st.number_input(
                "Sulfate", value=300.0
            )

        with col2:

            conductivity = st.number_input(
                "Conductivity", value=400.0
            )

            organic_carbon = st.number_input(
                "Organic Carbon", value=10.0
            )

            trihalomethanes = st.number_input(
                "Trihalomethanes", value=60.0
            )

            turbidity = st.number_input(
                "Turbidity", value=4.0
            )

        st.markdown("---")

        submitted = st.form_submit_button(
            "🔍 Analyse Water Sample",
            use_container_width=True
        )

    if submitted:

        input_data = pd.DataFrame([[
            ph,
            hardness,
            solids,
            chloramines,
            sulfate,
            conductivity,
            organic_carbon,
            trihalomethanes,
            turbidity
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

        prediction = model.predict(input_data)[0]

        st.markdown("---")

        st.markdown("### 📋 Analysis Result")

        if prediction == 1:

            st.success(
                "Dataset label prediction: POTABLE"
            )

        else:

            st.warning(
                "Dataset label prediction: NON-POTABLE"
            )

        st.caption(
            "Prediction generated using the AQUANTIS SVM model."
        )

    st.markdown("---")

    st.info(
        "Important: This is an educational machine-learning "
        "prediction, not a certified water-safety assessment. "
        "Never use this result alone to decide whether water "
        "is safe to drink."
    )


# DATA INSIGHTS PAGE

elif page == "Data Insights":

    st.html("""
    <div style="
        background: linear-gradient(120deg, #102C40, #07516B);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #168AAD;
        margin-bottom: 25px;
    ">
        <p style="color:#48CAE4; letter-spacing:2px;">
            AQUANTIS | DATA EXPLORATION
        </p>
        <h1 style="color:#F1FAFC;">
            Understanding Water Data
        </h1>
        <p style="color:#D5E8EF; font-size:16px;">
            Explore the dataset through visualisations,
            statistical patterns and feature relationships.
        </p>
    </div>
    """)

    st.markdown("### 📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Samples", "3,276")

    with col2:
        st.metric("Input Features", "9")

    with col3:
        st.metric("Target Classes", "2")

    st.markdown("---")

    st.markdown("### 🔍 Exploratory Data Analysis")

    st.write(
        "The following visualisations help us understand "
        "the distribution, missing values and relationships "
        "within the water quality dataset."
    )

    st.markdown("#### 1. Missing Values Analysis")

    st.image(
        "results/missing_values.png",
        use_container_width=True
    )

    st.caption(
        "This chart displays the number of missing values "
        "present in each dataset feature."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 2. Potability Distribution")

        st.image(
            "results/potability_distribution.png",
            use_container_width=True
        )

        st.caption(
            "Distribution of samples across the two "
            "potability classes."
        )

    with col2:
        st.markdown("#### 3. Feature Correlation")

        st.image(
            "results/correlation_heatmap.png",
            use_container_width=True
        )

        st.caption(
            "Correlation between different water quality "
            "parameters and the target variable."
        )

    st.markdown("---")

    st.markdown("#### 4. Feature Distributions")

    st.image(
        "results/feature_distributions.png",
        use_container_width=True
    )

    st.caption(
        "Distribution patterns of the nine water quality "
        "input parameters."
    )

    st.markdown("---")

    st.markdown("### 📋 Statistical Summary")

    summary = pd.read_csv("results/statistical_summary.csv")

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.info(
        "These insights describe patterns in the dataset. "
        "They do not independently establish whether a "
        "real-world water sample is safe to drink."
    )

# MODEL PERFORMANCE PAGE

elif page == "Model Performance":

    st.html("""
    <div style="
        background: linear-gradient(120deg, #102C40, #07516B);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #168AAD;
        margin-bottom: 25px;
    ">
        <p style="color:#48CAE4; letter-spacing:2px;">
            AQUANTIS | MODEL EVALUATION
        </p>
        <h1 style="color:#F1FAFC;">
            Model Performance
        </h1>
        <p style="color:#D5E8EF; font-size:16px;">
            Comparing machine learning algorithms to
            understand their predictive performance.
        </p>
    </div>
    """)

    st.markdown("### 🧠 Algorithm Comparison")

    st.write(
        "Four machine learning algorithms were evaluated "
        "using accuracy, precision, recall and F1-score."
    )

    comparison = pd.read_csv("results/model_comparison.csv")

    st.dataframe(
        comparison,
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("### 📊 Performance Metrics")

    metric_columns = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]

    selected_metric = st.selectbox(
        "Choose a metric to compare:",
        metric_columns
    )

    metric_mapping = {
        "Accuracy": "Accuracy",
        "Precision": "Precision",
        "Recall": "Recall",
        "F1 Score": "F1"
    }

    chart_column = metric_mapping[selected_metric]

    chart_data = comparison.set_index("Model")[[chart_column]]

    st.bar_chart(chart_data)

    st.markdown("---")

    st.markdown("### 🏆 Key Observations")

    st.write(
        "- SVM achieved the highest accuracy and precision "
        "among the evaluated models."
    )

    st.write(
        "- Decision Tree achieved the highest recall "
        "and F1-score."
    )

    st.write(
        "- Logistic Regression did not identify any positive "
        "samples in this evaluation."
    )

    st.info(
        "Accuracy alone does not describe the complete "
        "performance of a model. Precision, recall and "
        "F1-score provide additional insights."
    )

    st.markdown("---")

    st.markdown("### 🔬 Selected Model")

    st.success("Support Vector Machine (SVM)")

    st.write(
        "SVM was selected as the primary model for the "
        "AQUANTIS prediction interface because it achieved "
        "the highest accuracy in this evaluation."
    )

    st.warning(
        "The model has limitations, including relatively "
        "low recall. Its predictions are educational outputs "
        "and must not be treated as certified water-safety results."
    )

# ABOUT PAGE

elif page == "About":

    st.html("""
    <div style="
        background: linear-gradient(120deg, #102C40, #07516B);
        padding: 35px;
        border-radius: 18px;
        border: 1px solid #168AAD;
        margin-bottom: 25px;
    ">
        <p style="color:#48CAE4; letter-spacing:2px;">
            GET TO KNOW OUR PROJECT
        </p>
        <h1 style="color:#F1FAFC;">
            About AQUANTIS
        </h1>
        <p style="color:#D5E8EF; font-size:17px;">
            Intelligent Water Quality Analysis
        </p>
    </div>
    """)

    st.markdown("### 🌊 Our Project")

    st.write(
        "AQUANTIS is a machine learning-based water quality "
        "prediction project designed to explore how data "
        "science can contribute to water quality analysis."
    )

    st.write(
        "The system uses water quality parameters as input "
        "and applies a trained Support Vector Machine (SVM) "
        "model to predict the corresponding dataset potability label."
    )

    st.markdown("---")

    st.markdown("### 🎯 Project Objectives")

    st.markdown("""
    - Explore water quality data using Python.
    - Perform data preprocessing and exploratory data analysis.
    - Implement multiple machine learning algorithms.
    - Compare models using evaluation metrics.
    - Develop an interactive prediction interface.
    """)

    st.markdown("---")

    st.markdown("### ⚙️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Programming Language**")
        st.info("Python")

        st.markdown("**Machine Learning**")
        st.info("Scikit-learn")

        st.markdown("**Data Processing**")
        st.info("Pandas and NumPy")

    with col2:
        st.markdown("**Data Visualisation**")
        st.info("Matplotlib and Seaborn")

        st.markdown("**Frontend Framework**")
        st.info("Streamlit")

        st.markdown("**Model Storage**")
        st.info("Joblib")

    st.markdown("---")

    st.markdown("### 📁 Dataset Information")

    st.write(
        "Dataset: Water Potability Dataset"
    )

    st.write(
        "Source: Kaggle"
    )

    st.write(
        "Total Records: 3,276"
    )

    st.write(
        "Input Features: 9"
    )

    st.write(
        "Target Variable: Potability"
    )

    st.markdown(
        "[View Original Dataset](https://www.kaggle.com/"
        "datasets/adityakadiwal/water-potability)"
    )

    st.markdown("---")

    st.markdown("### ⚠️ Project Limitations")

    st.warning(
        "AQUANTIS is an educational machine learning project. "
        "Its predictions are based on patterns in the training "
        "dataset and are not a substitute for laboratory testing "
        "or certified water quality assessment."
    )

    st.markdown("---")

    st.markdown("### 💙 Our Vision")

    st.write(
        "To explore the potential of machine learning in "
        "understanding water quality data and making data-driven "
        "analysis more accessible."
    )

    st.markdown("---")

    st.markdown(
        "<div style='text-align:center; color:#48CAE4; "
        "padding:15px;'>"
        "<h3>AQUANTIS</h3>"
        "<p>Intelligent Water Quality Analysis</p>"
        "<p>Machine Learning-Based Water Quality Prediction</p>"
        "</div>",
        unsafe_allow_html=True
    )