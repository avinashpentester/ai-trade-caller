# storage/database.py
from sqlalchemy import create_engine
import os
from config import DB_PATH

def get_engine():
    return create_engine(f"sqlite:///{DB_PATH}", echo=False)

def save_to_db(symbol, df):
    try:
        table_name = symbol.replace(".", "_").lower()
        engine = get_engine()
        df.to_sql(table_name, con=engine, if_exists="replace", index=True)
        print(f"✅ Data saved for {symbol} into {table_name}")
    except Exception as e:
        print(f"❌ Error saving {symbol} to DB: {e}")
