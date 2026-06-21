def add_ema(data, window=20):
    """
    Calculate Exponential Moving Average (EMA)

    Parameters:
        data (DataFrame): Stock data
        window (int): Number of periods

    Returns:
        DataFrame: Updated dataframe with EMA column
    """

    data["EMA"] = data["Close"].ewm(
        span=window,
        adjust=False
    ).mean()

    return data