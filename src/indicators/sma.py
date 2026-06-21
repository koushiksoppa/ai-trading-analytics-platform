def add_sma(data, window=20):
    """
    Calculate Simple Moving Average (SMA)

    Parameters:
        data (DataFrame): Stock data
        window (int): Number of periods

    Returns:
        DataFrame: Updated dataframe with SMA column
    """

    data["SMA"] = data["Close"].rolling(window=window).mean()

    return data