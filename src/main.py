from data.data_loader import (
    download_stock_data,
    save_data_to_csv
)

from indicators.sma import add_sma
from indicators.ema import add_ema
from indicators.rsi import add_rsi
from indicators.macd import add_macd
from indicators.bollinger import add_bollinger_bands

from analytics.risk_analysis import (
    calculate_daily_returns,
    calculate_volatility,
    calculate_sharpe_ratio,
    calculate_max_drawdown
)

from analytics.trend_analysis import analyze_trend

from visualization.charts import (
    plot_price_chart,
    plot_rsi,
    plot_macd,
    plot_bollinger_bands
)


def main():

    print("=" * 60)
    print("AI TRADING ANALYTICS PLATFORM")
    print("=" * 60)

    ticker = input(
        "\nEnter Stock Symbol (Example: RELIANCE.NS): "
    ).upper()

    print(f"\nDownloading {ticker} data...\n")

    data = download_stock_data(ticker)

    if data is None:
        print("Unable to fetch stock data.")
        return

    save_data_to_csv(data, ticker)

    # Technical Indicators
    data = add_sma(data)
    data = add_ema(data)
    data = add_rsi(data)
    data = add_macd(data)

    print("\n========== DEBUG ==========")
    print(data.columns)
    print("\nType of data['Close']:")
    print(type(data["Close"]))
    print("===========================\n")

    data = add_bollinger_bands(data)

    # Risk Metrics
    data = calculate_daily_returns(data)

    volatility = calculate_volatility(data)
    sharpe_ratio = calculate_sharpe_ratio(data)
    max_drawdown = calculate_max_drawdown(data)

    # Trend Analysis
    trend_result = analyze_trend(data)

    print("\n" + "=" * 60)
    print("ANALYSIS REPORT")
    print("=" * 60)

    print(f"Stock: {ticker}")
    print(f"Current Price: {trend_result['Close']}")
    print(f"RSI: {trend_result['RSI']}")
    print(f"Trend: {trend_result['Trend']}")
    print(f"Recommendation: {trend_result['Recommendation']}")
    print(f"Volatility: {volatility}%")
    print(f"Sharpe Ratio: {sharpe_ratio}")
    print(f"Maximum Drawdown: {max_drawdown}%")

    print("=" * 60)

    # Charts
    plot_price_chart(data, ticker)
    plot_rsi(data)
    plot_macd(data)
    plot_bollinger_bands(data)


if __name__ == "__main__":
    main()

