# 📊 Analysis Summary – Credit Risk Modelling

## 🧾 Data Description

The dataset contains information such as:
- Age, Annual Income
- Loan amount & tenure
- Credit utilization, delinquency ratio, DPD
- Loan type, purpose, and residence type

## 🔍 Feature Engineering

- `loan_to_income`: loan amount ÷ annual income
- One-hot encoding for: residence type, loan purpose, loan type
- Normalized features using MinMaxScaler
- Added default constants for missing input features

## ⚙️ Model

- Model: Logistic Regression
- Output: Probability of default
- Score: Converted to 300–900 credit score scale

## 💡 Insights

- Higher income, fewer active loans, and low credit utilization = lower risk.
- Credit utilization and DPD have strong impact on risk rating.