import os
import django


# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stocksite.settings")
django.setup()

import numpy as np
import joblib
from tensorflow.keras.models import load_model
from predictor.preprocessing import preprocess_stock_data
import matplotlib.pyplot as plt

def predict_stock_trend(symbol="MSFT", window_size=30):
  
    X, y, scaler = preprocess_stock_data(symbol, window_size)
    if X is None or len(X) == 0:
        return None
    
  
    model = load_model("predictor/saved_model/stock_lstm_model.h5")
    
   
    latest_sequence = X[-1:]  # shape = (1, 30, 5)

    prediction = model.predict(latest_sequence)
    predicted_trend = 1 if prediction[0][0] > 0.5 else 0

    return "UP" if predicted_trend == 1 else "DOWN"
