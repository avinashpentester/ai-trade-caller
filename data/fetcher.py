# data/fetcher.py
import yfinance as yf
from nsetools import Nse
import time

def get_all_stock_symbols():
    nse = Nse()
    codes = nse.get_stock_codes()
    return [symbol + ".NS" for symbol in list(codes.keys())[1:]]  # skip header

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