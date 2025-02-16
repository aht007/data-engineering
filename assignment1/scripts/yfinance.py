import os
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=2*365)).strftime('%Y-%m-%d')

def fetch_ticker_data(ticker):
    """Fetch historical close prices for a single ticker (stock)."""
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df['Close']

def read_data(tickers):
    """Fetch 'Close' prices for the given tickers from Yahoo Finance."""
    return {ticker: fetch_ticker_data(ticker) for ticker in tickers}

def save_to_csv(data, filepath, filename):
    """Save the collected ticker (stock) data to a CSV file."""
    df = pd.DataFrame(data)
    # Check if filepath directory doesn't exist and create it
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    filepath = os.path.join(filepath, filename)
    df.to_csv(filepath, index=True)
    print(f"Data saved to {filepath}")

ev_tickers = ["TSLA", "BYDDY", "LCID", "VOW3.DE", "RIVN", "BMW.DE", "MBG.DE"]

ev_data = read_data(ev_tickers, start_date, end_date)
save_to_csv(ev_data, 'datasets/raw/', 'yfinance.csv')
