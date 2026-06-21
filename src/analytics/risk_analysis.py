import numpy as np


def calculate_daily_returns(data):
    """
    Calculate daily percentage returns.
    """

    data["Daily_Return"] = data["Close"].pct_change()

    return data


def calculate_volatility(data):
    """
    Calculate annualized volatility.
    """

    volatility = (
        data["Daily_Return"].std() * np.sqrt(252)
    ) * 100

    return round(volatility, 2)


def calculate_sharpe_ratio(data, risk_free_rate=0.05):
    """
    Calculate Sharpe Ratio.
    """

    daily_rf = risk_free_rate / 252

    excess_returns = (
        data["Daily_Return"] - daily_rf
    )

    sharpe_ratio = (
        np.sqrt(252)
        * excess_returns.mean()
        / excess_returns.std()
    )

    return round(sharpe_ratio, 2)


def calculate_max_drawdown(data):
    """
    Calculate Maximum Drawdown.
    """

    cumulative_max = data["Close"].cummax()

    drawdown = (
        (data["Close"] - cumulative_max)
        / cumulative_max
    )

    max_drawdown = drawdown.min() * 100

    return round(max_drawdown, 2)