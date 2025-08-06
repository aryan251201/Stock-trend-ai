import yfinance as yf
from .models import StockData
from datetime import datetime

def fetch_stock_data(ticker, period="6mo", interval="1d"):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)

        if hist.empty:
            return None

        hist.reset_index(inplace=True)
        hist["Date"] = hist["Date"].dt.date  # convert to date object

        for _, row in hist.iterrows():
            StockData.objects.update_or_create(
                symbol=ticker.upper(),
                date=row["Date"],
                defaults={
                    "open": row["Open"],
                    "high": row["High"],
                    "low": row["Low"],
                    "close": row["Close"],
                    "volume": int(row["Volume"]),
                }
            )

        return hist[["Date", "Open", "High", "Low", "Close", "Volume"]].to_dict(orient="records")

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None
