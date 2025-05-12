# signals/strategy_engine.py
import pandas as pd

def generate_signal(df):
    if 'Close' not in df.columns:
        return None
    df['RSI'] = compute_rsi(df['Close'], 14)
    latest = df.iloc[-1]
    if latest['RSI'] < 30:
        return "BUY"
    elif latest['RSI'] > 70:
        return "SELL"
    return None

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi