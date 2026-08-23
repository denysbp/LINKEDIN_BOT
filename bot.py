import os
from logging_config import configure_logging
configure_logging(os.getenv("LOG_LEVEL", "INFO"))
import logging
from database import init_db
from core.pipeline import process_jobs
from services.linkedin import LinkedInClient
from services.parser import Parser
from services.notifier import TelegramNotifier
from config import KEYWORDS, LOCATION, ensure_telegram_configured
import sys

logger = logging.getLogger("TELEGRAM-BOT")


try:
    ensure_telegram_configured()
    init_db()
except Exception:
    logger.warning("Telegram não configurado;")
    sys.exit(1)

client = LinkedInClient()
parser = Parser()
notifier = TelegramNotifier()


if __name__ == "__main__":
    html = client.fetch(KEYWORDS, LOCATION)
    jobs = parser.parse(html)

    process_jobs(jobs, notifier)
