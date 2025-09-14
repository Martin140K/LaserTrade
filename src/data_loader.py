# import yfinance as yf
# import pandas as pd

# def load_data():
#     # stáhne BTC data za posledních 2 roky
#     df = yf.download('AAPL', period='2y', interval='1d')
#     df.reset_index(inplace=True)
#     return df


# import yfinance as yf
# import pandas as pd

# def load_data(ticker="BTC-USD", period="2y", interval="1d"):
#     """
#     Stáhne data z Yahoo Finance pro zadaný ticker.
#     Defaultně bere BTC-USD, ale můžeš dát třeba AAPL.
#     """
#     df = yf.download(ticker, period=period, interval=interval)
#     df.dropna(inplace=True)
#     return df

import yfinance as yf
import pandas as pd

def load_data(ticker):
    """
    Načte historická data pro zadaný ticker.
    """
    df = yf.download(ticker, period="10y", interval="1d")
    df.reset_index(inplace=True)  # aby měl sloupec 'Date'
    df.rename(columns={'Adj Close': 'Close'}, inplace=True)
    return df
