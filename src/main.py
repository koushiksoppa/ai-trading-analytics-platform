import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def download_stock_data(ticker, period="1y"):
    data = yf.download(ticker, period=period)
    return data


def show_basic_info(data):
    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nLast 5 Rows:")
    print(data.tail())

    print("\nShape:")
    print(data.shape)


def plot_stock_price(data, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(data["Close"])

    plt.title(f"{ticker} Closing Price")

    plt.xlabel("Date")

    plt.ylabel("Price (INR)")

    plt.grid(True)

    plt.show()


ticker = "RELIANCE.NS"

data = download_stock_data(ticker)

show_basic_info(data)

plot_stock_price(data, ticker)

