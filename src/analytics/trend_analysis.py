def analyze_trend(data):
    """
    Analyze stock trend using SMA, EMA, RSI and MACD.

    Returns:
        dict containing trend information
    """

    latest = data.iloc[-1]

    close_price = latest["Close"]
    sma = latest["SMA"]
    ema = latest["EMA"]
    rsi = latest["RSI"]
    macd = latest["MACD"]
    signal = latest["Signal"]

    trend = "NEUTRAL"
    recommendation = "HOLD"

    # Bullish Conditions
    if (
        close_price > sma
        and close_price > ema
        and macd > signal
        and rsi < 70
    ):
        trend = "BULLISH"
        recommendation = "BUY"

    # Bearish Conditions
    elif (
        close_price < sma
        and close_price < ema
        and macd < signal
        and rsi > 30
    ):
        trend = "BEARISH"
        recommendation = "SELL"

    return {
        "Trend": trend,
        "Recommendation": recommendation,
        "RSI": round(rsi, 2),
        "Close": round(close_price, 2)
    }