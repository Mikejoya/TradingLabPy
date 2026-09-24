import os

from dotenv import load_dotenv

from data.sources.alpha_vantage import AlphaVantageClient
from data.transformers.price_transformer import transform_candle

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

client = AlphaVantageClient(api_key)

data = client.get__daily_price("SPY")

time_series = data["Time Series (Daily)"]

candles = transform_candle(time_series)

print(candles[0])
print("Total de velas:", len(candles))
