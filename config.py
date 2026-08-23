try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*a, **k):
        return None

import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
KEYWORDS = os.getenv("KEYWORDS")
LOCATION = os.getenv("LOCATION")
DB_NAME = os.getenv("DB_NAME_ENV")

def ensure_telegram_configured():
    keys = [
        TELEGRAM_TOKEN,
        CHAT_ID,
        KEYWORDS,
        LOCATION,
        DB_NAME
    ]
    if not any(keys):
        raise ValueError("Variáveis de ambiente configuradas!")