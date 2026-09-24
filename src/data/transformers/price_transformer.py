def transform_candle(time_series):
    candles = []
    for date, candle in time_series.items():
        transformed = {
            "date": date,
            "open": float(candle["1. open"]),
            "high": float(candle["2. high"]),
            "low": float(candle["3. low"]),
            "close": float(candle["4. close"]),
            "volume": int(candle["5. volume"]),
        }
        candles.append(transformed)
    return candles
