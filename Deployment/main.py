import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import tensorflow as tf
import tensorflow_recommenders as tfrs

os.environ["TF_USE_LEGACY_KERAS"] = "1"

# Inisialisasi Aplikasi FastAPI
app = FastAPI(title="SugarCoat.ai API", description="API untuk Prediksi Risiko Diabetes Berdasarkan Gaya")

# Load model secara global
MODEL_PATH = "sugarcoat_model.keras"
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    raise RuntimeError("Gawat! File model .keras tidak ditemukan di server.")

# Skema Request
class UserLifestyle(BaseModel):
    age: int
    gender: str
    employment_status: str
    smoking_status: str
    alcohol_consumption_per_week: int
    physical_activity_minutes_per_week: int
    sleep_hours_per_day: float
    screen_time_hours_per_day: float
    family_history_diabetes: int
    hypertension_history: int
    cardiovascular_history: int
    bmi: float
    sweet_beverages_per_week: int

# Hardcoded Mapping 
GENDER_MAP = {'Female': 0, 'Male': 1}
EMP_MAP = {'Employed': 0, 'Retired': 1, 'Student': 2, 'Unemployed': 3}
SMOKE_MAP = {'Current': 0, 'Former': 1, 'Never': 2}

@app.get("/")
def home():
    return {"message": "SugarCoat ML API is Running! Tembak endpoint /predict untuk inferensi."}

@app.post("/predict")
def predict_risk(data: UserLifestyle):
    try:
        # Konversi request JSON menjadi Dictionary
        user_dict = data.model_dump()
        
        # Mapping Teks ke Angka
        # Jika web mengirim teks typo ('Pria'), beri default 0 agar tidak crash
        user_dict['gender'] = GENDER_MAP.get(user_dict['gender'], 0)
        user_dict['employment_status'] = EMP_MAP.get(user_dict['employment_status'], 0)
        user_dict['smoking_status'] = SMOKE_MAP.get(user_dict['smoking_status'], 2)
        
        # Ubah ke DataFrame
        df_input = pd.DataFrame({k: [v] for k, v in user_dict.items()})
        
        # Inferensi Model
        raw_pred = model.predict(df_input, verbose=0)
        probabilitas = float(raw_pred[0][0])
        
        # Siapkan Response
        is_risky = probabilitas >= 0.5
        
        return {
            "status": "success",
            "is_risky": is_risky,
            "probability": round(probabilitas, 4),
            "roast_trigger": "SICK" if is_risky else "HEALTHY" # Hint untuk Model Gen-AI
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))