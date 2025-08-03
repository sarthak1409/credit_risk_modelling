# CredSure: Smart Credit Risk Modelling 🧠📊

CredSure is an interactive Streamlit web application designed to predict **credit risk** based on user-provided personal and financial data. This tool uses a machine learning model to estimate the likelihood of default and generate a credit score and risk rating.

## 🚀 Features

- Predicts default probability using ML
- Calculates credit score (300–900 scale)
- Provides risk rating: Excellent, Good, Average, Poor
- Clean UI with Streamlit
- Responsive background and UI for mobile/desktop

## 🧩 How it works

Input user financial data and let the model, trained on historical credit data, estimate credit risk. It uses a logistic regression model with engineered features and scaled inputs.

## 📁 Folder Structure

```
credit_risk_modelling/
├── app/
│   ├── main.py
│   ├── prediction_helper.py
│   ├── artifacts/
│   │   └── model_data.joblib
│   ├── images/
│   │   └── background_image.avif
│   └── datasets/ (not uploaded)
├── notebook/
│   └── credit_risk_notebook.ipynb
└── README.md
```

## 📦 Setup Instructions

1. Clone the repository
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:  
   ```bash
   streamlit run main.py
   ```

## ⚠️ Disclaimer

- This application is built for **educational purposes only**.
- The model and data used are illustrative and **not suitable for production**.
- The dataset used is **confidential** and not uploaded publicly.