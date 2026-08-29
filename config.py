try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*a, **k):
        return None

import os
import sys

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
KEYWORDS = os.getenv("KEYWORDS")
LOCATION = os.getenv("LOCATION")
DB_NAME = os.getenv("DB_NAME_ENV")
LIMIT = int(os.getenv("MESSAGE_LIMIT", 0))
FLASK_PORT = os.getenv("FLASK_PORT")

def create_env():
    FILE_NAME = ".env"
    try:
        with open(FILE_NAME, "w+") as env:
            env.write(
                "TELEGRAM_TOKEN=<telegram-token>\n"
                "CHAT_ID=<chat-id>\n"
                "KEYWORDS=<jobs keywords>\n"
                "DB_NAME='jobs.db'\n"
                'LOCATION="Portugal"\n'
                'MESSAGE_LIMIT=20\n'
                'LOG_LEVEL="info"\n'
                'FLASK_PORT=8080\n'
            )
    except IOError as e:
        print(e)
        sys.exit(1)

def ensure_telegram_configured():
    keys = [
        TELEGRAM_TOKEN,
        CHAT_ID,
        KEYWORDS,
        LOCATION,
        DB_NAME,
        LIMIT,
        FLASK_PORT
    ]
    if not any(keys):
        print("Variáveis de ambiente configuradas!")
        create_env()
        print(".ENV FILE CREATED")
        sys.exit(1)