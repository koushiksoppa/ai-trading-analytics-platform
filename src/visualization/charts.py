import matplotlib.pyplot as plt


def plot_price_chart(data, ticker):
    """
    Plot Price, SMA and EMA
    """

    plt.figure(figsize=(14, 7))

    plt.plot(data.index, data["Close"], label="Close Price")
    plt.plot(data.index, data["SMA"], label="SMA 20")
    plt.plot(data.index, data["EMA"], label="EMA 20")

    plt.title(f"{ticker} Price Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()
    plt.grid(True)

    plt.show()


def plot_rsi(data):
    """
    Plot RSI
    """

    plt.figure(figsize=(14, 4))

    plt.plot(data.index, data["RSI"], label="RSI")

    plt.axhline(70, linestyle="--")
    plt.axhline(30, linestyle="--")

    plt.title("RSI Indicator")

    plt.legend()
    plt.grid(True)

    plt.show()


def plot_macd(data):
    """
    Plot MACD
    """

    plt.figure(figsize=(14, 5))

    plt.plot(data.index, data["MACD"], label="MACD")
    plt.plot(data.index, data["Signal"], label="Signal")

    plt.title("MACD Indicator")

    plt.legend()
    plt.grid(True)

    plt.show()


def plot_bollinger_bands(data):
    """
    Plot Bollinger Bands
    """

    plt.figure(figsize=(14, 7))

    plt.plot(data.index, data["Close"], label="Close Price")
    plt.plot(data.index, data["BB_Upper"], label="Upper Band")
    plt.plot(data.index, data["BB_Middle"], label="Middle Band")
    plt.plot(data.index, data["BB_Lower"], label="Lower Band")

    plt.title("Bollinger Bands")

    plt.legend()
    plt.grid(True)

    plt.show()