import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stocksite.settings")
django.setup()

from predictor.preprocessing import preprocess_stock_data

X, y, scaler = preprocess_stock_data("MSFT")

if X is None or y is None:
    print(" Not enough data or symbol not found.")
else:
    print(f" X shape: {X.shape}")
    print(f" y shape: {y.shape}")
    print(" Sample X[0]:")
    print(X[0])
    print(" Sample y[0]:")
    print(y[0])
