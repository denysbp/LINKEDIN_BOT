try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*a, **k):
        return None

import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def ensure_telegram_configured():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise ValueError("Variáveis de ambiente TELEGRAM_TOKEN/CHAT_ID não configuradas!")

KEYWORDS = os.getenv("KEYWORDS", "backend python java junior")
LOCATION = os.getenv("LOCATION", "Portugal")