import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from .models import StockData

def get_stock_dataframe(symbol):
    
    queryset = StockData.objects.filter(symbol=symbol.upper()).order_by("date")
    if not queryset.exists():
        return None

    df = pd.DataFrame.from_records(queryset.values())
    df.set_index("date", inplace=True)
    return df[["open", "high", "low", "close", "volume"]]


def preprocess_stock_data(symbol, window_size=30):

    df = get_stock_dataframe(symbol)
    if df is None or len(df) < window_size + 1:
        return None, None, None

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)

    X = []
    y = []

    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i - window_size:i])
        y.append(scaled_data[i][3])  # 3 = 'close'

    X = np.array(X)
    y = np.array(y)

    return X, y, scaler

