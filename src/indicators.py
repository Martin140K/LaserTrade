import pandas as pd

def add_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def add_ema(df, span=20):
    df[f'EMA_{span}'] = df['Close'].ewm(span=span, adjust=False).mean()
    return df
