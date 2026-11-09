import os
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='../templates')

# Path lokasi file model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model_dt_churn.joblib')
COLUMNS_PATH = os.path.join(BASE_DIR, 'model', 'model_columns.joblib')

# Load model & columns
model = joblib.load(MODEL_PATH)
model_columns = joblib.load(COLUMNS_PATH)


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    prob_text = None

    if request.method == 'POST':
        # Tangkap data dari form web
        tenure = float(request.form.get('tenure', 0))
        monthly_charges = float(request.form.get('MonthlyCharges', 0))
        total_charges = float(request.form.get('TotalCharges', 0))
        contract = request.form.get('Contract', 'Month-to-month')
        internet_service = request.form.get('InternetService', 'Fiber optic')

        # Buat dataframe input awal
        input_dict = {
            'tenure': tenure,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges,
            f'Contract_{contract}': 1 if f'Contract_{contract}' in model_columns else 0,
            f'InternetService_{internet_service}': 1 if f'InternetService_{internet_service}' in model_columns else 0
        }

        input_df = pd.DataFrame([input_dict])
        # Reindex agar kolom persis sama dengan training data
        input_df = input_df.reindex(columns=model_columns, fill_value=0)

        # Prediksi
        pred = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1] * 100

        if pred == 1:
            prediction_text = "Pelanggan Berpotensi CHURN (Berhenti Berlangganan)"
        else:
            prediction_text = "Pelanggan Diprediksi SETIA (Bertahan Berlangganan)"

        prob_text = f"Probabilitas Churn: {prob:.1f}%"

    return render_template('index.html', prediction_text=prediction_text, prob_text=prob_text)


# Untuk running lokal
if __name__ == '__main__':
    app.run(debug=True)
