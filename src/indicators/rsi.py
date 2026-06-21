import pandas as pd


def add_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI)

    Parameters:
        data (DataFrame): Stock data
        window (int): RSI period

    Returns:
        DataFrame: Updated dataframe with RSI column
    """

    delta = data["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (100 / (1 + rs))

    return data