import pandas as pd

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

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

def add_indicators(df):
    df['EMA_20'] = df['Close'].ewm(span=20, min_periods=1).mean()
    df['RSI'] = compute_rsi(df['Close'])
    return df