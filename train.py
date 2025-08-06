import numpy as np
from predictor.preprocessing import preprocess_stock_data
from predictor.model import build_lstm_model
import os
import sys

# Add the root project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocksite.settings')

import django
django.setup()



# Load data
X, y, scaler = preprocess_stock_data("MSFT", window_size=30)

if X is None:
    print("Not enough data to train.")
else:
    model = build_lstm_model((X.shape[1], X.shape[2]))
    model.fit(X, y, epochs=20, batch_size=16)

    # Save model
    model.save("predictor/saved_model/stock_lstm_model.h5")
    print("Model trained and saved.")
