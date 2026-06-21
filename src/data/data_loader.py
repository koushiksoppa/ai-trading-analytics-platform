import os
import yfinance as yf
import pandas as pd


def download_stock_data(ticker, period="1y"):
    """
    Download stock data from Yahoo Finance.
    """

    try:
        data = yf.download(
            ticker,
            period=period,
            auto_adjust=True,
            progress=False
        )

        # Fix MultiIndex columns from yfinance
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        if data.empty:
            raise ValueError(f"No data found for {ticker}")

        return data

    except Exception as e:
        print(f"Error downloading {ticker}: {e}")
        return None


def save_data_to_csv(data, ticker):
    """
    Save stock data to CSV file.
    """

    os.makedirs("data/raw", exist_ok=True)

    file_path = f"data/raw/{ticker}.csv"

    data.to_csv(file_path)

    print(f"\nData saved successfully: {file_path}")


def load_data_from_csv(ticker):
    """
    Load stock data from CSV.
    """

    file_path = f"data/raw/{ticker}.csv"

    if os.path.exists(file_path):
        return pd.read_csv(
            file_path,
            index_col=0,
            parse_dates=True
        )

    print(f"{file_path} not found.")

    return None