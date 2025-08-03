import streamlit as st
from prediction_helper import predict
import base64
import time

st.set_page_config(page_title="CredSure: Smart Credit Risk Modelling", page_icon="📊", layout="centered")

st.sidebar.title("📘 About This App")
st.sidebar.markdown("### 🔍 Use the sidebar to understand input fields.")

with st.sidebar.expander("ℹ️ Full Project Info", expanded=True):
    st.markdown("""
    **CredSure: Smart Credit Risk Modelling**

    This app predicts the **credit risk** of a user based on personal and financial inputs using a machine learning model.

    ---
    ### 📌 Feature Descriptions

    - **Age**: Applicant's age in years.  
    - **Annual Income (₹)**: Gross yearly income.  
    - **Number of Active Loans**: Currently active credit accounts.  
    - **Avg Days Past Due (DPD)**: Overdue days on past loans.  
    - **Delinquency Ratio (%)**: Delinquent months relative to loan tenure.  
    - **Credit Utilization (%)**: Used credit vs total credit available.  
    - **Loan Amount (₹)**: Requested loan amount.  
    - **Loan Tenure (Months)**: Duration of the loan.  
    - **Residence Type**: Owned / Rented / Mortgage.  
    - **Loan Purpose**: Education, Home, Auto, etc.  
    - **Loan Type**: Secured (with collateral) or Unsecured.  

    ---
    ### ⚠️ Disclaimer
    This tool is for **educational purposes only**.
    
    It is not intended for real financial decision-making. Please input realistic values for meaningful outputs.
    """)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-position: center top;
            background-repeat: no-repeat;
            background-attachment: scroll;
            background-color: #f5f7fa;
            background-size: cover;     
            min-height: 100vh;
        }}

        @media (max-width: 768px) {{
            .stApp {{
                background-size: contain !important;  
                background-position: top center;
                background-repeat: no-repeat;
            }}
        }}

        html, body {{
            height: auto;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



add_bg_from_local("images/filters_format(webp)_quality(80).avif")

st.markdown("""
    <style>
    .section {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        margin-bottom: 25px;
    }
    .stButton button {
        background-color: #1abc9c;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
    }
    .stButton button:hover {
        background-color: #16a085;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>CredSure</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #7f8c8d;'>Smart Credit Risk Modelling DashBoard</h4>", unsafe_allow_html=True)

with st.container():
    st.subheader(":gray[**👤 Personal & Credit Profile**]")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input(":gray[**Age**]", min_value=18, max_value=100, value=28)
    with col2:
        income = st.number_input(":gray[**Annual Income (₹)**]", min_value=0, value=1000000)
    with col3:
        num_open_accounts = st.number_input(":gray[**Number of Active Loans**]", min_value=1, max_value=10, value=2)

    col4, col5, col6 = st.columns(3)
    with col4:
        avg_dpd_per_delinquency = st.number_input(":gray[**Avg Days Past Due (DPD)**]", min_value=0, value=20)
    with col5:
        delinquency_ratio = st.slider(":gray[**Delinquency Ratio (%)**]", 0, 100, 30)
    with col6:
        credit_utilization_ratio = st.slider(":gray[**Credit Utilization (%)**]", 0, 100, 30)

with st.container():
    st.subheader(":gray[**💰 Loan Details**]")

    col7, col8, col9 = st.columns(3)
    with col7:
        loan_amount = st.number_input(":gray[**Loan Amount (₹)**]", min_value=0, value=200000)
    with col8:
        loan_tenure_months = st.number_input(":gray[**Loan Tenure (Months)**]", min_value=0, value=36)
    with col9:
        loan_to_income_ratio = loan_amount / income if income > 0 else 0
        st.markdown(f"""
            <div style='
                background-color: #ecf0f1;
                color: #34495e;
                font-weight: 600;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                font-size: 16px;
                border: 1px solid #ccc;
            '>
                Loan to Income Ratio<br>
                <span style='font-size: 22px; font-weight: bold;'>{loan_to_income_ratio:.2f}</span>
            </div>
        """, unsafe_allow_html=True)

    col10, col11, col12 = st.columns(3)
    with col10:
        residence_type = st.selectbox(":gray[**Residence Type**]", ['Owned', 'Rented', 'Mortgage'])
    with col11:
        loan_purpose = st.selectbox(":gray[**Loan Purpose**]", ['Education', 'Home', 'Auto', 'Personal'])
    with col12:
        loan_type = st.selectbox(":gray[**Loan Type**]", ['Unsecured', 'Secured'])


with st.container():
    st.subheader(":gray[**🎯 Predict Credit Risk**]")

    if st.button("📈 Calculate Risk"):
        with st.spinner(':blue[**Analyzing your profile and calculating risk...**]'):
            time.sleep(2)

            probability, credit_score, rating = predict(
                age=age,
                income=income,
                loan_amount=loan_amount,
                loan_tenure_months=loan_tenure_months,
                avg_dpd_per_delinquency=avg_dpd_per_delinquency,
                loan_type=loan_type,
                delinquent_months_to_loan_months=delinquency_ratio,
                credit_utilization_ratio=credit_utilization_ratio,
                num_open_accounts=num_open_accounts,
                residence_type=residence_type,
                loan_purpose=loan_purpose,
            )

        st.success(":grey[**✅ Risk Prediction Completed**]")

        rating_color = {
            "Excellent": "#27ae60",
            "Good": "#2ecc71",
            "Average": "#f39c12",
            "Poor": "#e74c3c",
            "Very Poor": "#c0392b"
        }.get(rating, "#7f8c8d")

        colA, colB, colC = st.columns(3)
        with colA:
            st.markdown(f"""
                <div style='
                    background-color: #ecf0f1;
                    color: #34495e;
                    font-weight: 600;
                    padding: 10px;
                    border-radius: 8px;
                    text-align: center;
                    font-size: 16px;
                    border: 1px solid #ccc;
                '>
                    Default Probability<br>
                    <span style='font-size: 22px; font-weight: bold;'>{probability:.2%}</span>
                </div>
            """, unsafe_allow_html=True)

        with colB:
            st.markdown(f"""
                <div style='
                    background-color: #ecf0f1;
                    color: #34495e;
                    font-weight: 600;
                    padding: 10px;
                    border-radius: 8px;
                    text-align: center;
                    font-size: 16px;
                    border: 1px solid #ccc;
                '>
                    Credit Score<br>
                    <span style='font-size: 22px; font-weight: bold;'>{credit_score}</span>
                </div>
            """, unsafe_allow_html=True)

        with colC:
            st.markdown(
                f"<div style='padding: 10px; border-radius: 10px; background-color: {rating_color}; color: white; text-align: center; font-weight: bold;'>{rating}</div>",
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)
