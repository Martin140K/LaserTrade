import yfinance as yf
import pandas as pd

def load_data():
    # stáhne BTC data za posledních 2 roky
    df = yf.download('BTC-USD', period='2y', interval='1d')
    df.reset_index(inplace=True)
    return df