from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import fetch_stock_data

@api_view(["POST"])
def get_stock_data(request):
    ticker = request.data.get("ticker", "AAPL")  # default to AAPL if not provided
    data = fetch_stock_data(ticker)

    if data is None:
        return Response({"error": "Invalid ticker or no data available"}, status=400)

    return Response({"ticker": ticker, "data": data})
