def add_bollinger_bands(data, window=20):
    """
    Calculate Bollinger Bands

    Parameters:
        data (DataFrame): Stock data
        window (int): Rolling window period

    Returns:
        DataFrame: Updated dataframe with Bollinger Bands
    """

    data["BB_Middle"] = data["Close"].rolling(
        window=window
    ).mean()

    rolling_std = data["Close"].rolling(
        window=window
    ).std()

    data["BB_Upper"] = (
        data["BB_Middle"] + (rolling_std * 2)
    )

    data["BB_Lower"] = (
        data["BB_Middle"] - (rolling_std * 2)
    )

    return data