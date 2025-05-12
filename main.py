# main.py
from data.fetcher import get_all_stock_symbols, fetch_stock_data
from storage.database import save_to_db
from signals.strategy_engine import generate_signal
from alerts.whatsapp_bot import send_whatsapp_message
from utils.scheduler import start_scheduler
from config import FETCH_INTERVAL_MINUTES

symbols = get_all_stock_symbols()

def monitor():
    print("🔄 Fetching stock data...")
    data = fetch_stock_data(symbols, interval="5m", period="1d")
    for symbol, df in data.items():
        signal = generate_signal(df)
        if signal:
            save_to_db(symbol, df)
            msg = f"📈 Trade Signal for {symbol}\nAction: {signal}\nLast Price: ₹{df['Close'].iloc[-1]:.2f}"
            send_whatsapp_message(msg)

if __name__ == "__main__":
    start_scheduler(monitor, FETCH_INTERVAL_MINUTES)
    while True:
        pass  # Keep the script running