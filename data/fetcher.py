# data/fetcher.py
import yfinance as yf
import pandas as pd
import requests
import time

def get_all_stock_symbols():
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    df = pd.read_csv(pd.compat.StringIO(r.text))
    return [symbol + ".NS" for symbol in df['SYMBOL'].tolist()]

def fetch_stock_data(symbols, interval="1d", period="5d"):
    data = {}
    for symbol in symbols:
        try:
            df = yf.download(symbol, period=period, interval=interval, progress=False)
            if not df.empty:
                df['Symbol'] = symbol
                data[symbol] = df
                print(f"✔️ {symbol} data fetched")
            time.sleep(1)  # Avoid rate limit
        except Exception as e:
            print(f"❌ {symbol} failed: {e}")
    return data
