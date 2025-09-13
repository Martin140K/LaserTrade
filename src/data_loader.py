import yfinance as yf
import pandas as pd

def load_data(ticker="BTC-USD", period="2y", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df