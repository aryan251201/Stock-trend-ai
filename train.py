
import numpy as np
from sklearn.model_selection import train_test_split
import os
import sys
import django

# Django setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocksite.settings')
django.setup()

from predictor.preprocessing import preprocess_stock_data
from predictor.model import build_lstm_model

X, y, scaler = preprocess_stock_data("MSFT", window_size=30)

if X is None:
    print("Not enough data to train.")
else:
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    
    model = build_lstm_model((X.shape[1], X.shape[2]))

   
    model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_test, y_test))

    
    model.save("predictor/saved_model/stock_lstm_model.h5")
    print("Model trained and saved.")


loss, accuracy = model.evaluate(X_test, y_test)

