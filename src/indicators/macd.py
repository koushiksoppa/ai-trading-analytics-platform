def add_macd(data):
    """
    Calculate MACD (Moving Average Convergence Divergence)

    Parameters:
        data (DataFrame): Stock data

    Returns:
        DataFrame: Updated dataframe with MACD columns
    """

    ema_12 = data["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema_26 = data["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    data["MACD"] = ema_12 - ema_26

    data["Signal"] = data["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    data["Histogram"] = data["MACD"] - data["Signal"]

    return data