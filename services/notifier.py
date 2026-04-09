import requests
import logging
from config import TELEGRAM_TOKEN, CHAT_ID, ensure_telegram_configured

logger = logging.getLogger(__name__)


class TelegramNotifier:
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        try:
            ensure_telegram_configured()
        except Exception:
            if not self.dry_run:
                raise
            logger.warning("Telegram não configurado; modo dry_run ativado")

    def send(self, message: str) -> bool:
        if self.dry_run:
            logger.info("[dry_run] Mensagem Telegram: %s", message)
            return True

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        try:
            res = requests.post(url, json={
                "chat_id": CHAT_ID,
                "text": message
            }, timeout=10)
            res.raise_for_status()
            return True
        except requests.RequestException as e:
            logger.exception("Erro ao enviar mensagem Telegram: %s", e)
            return False

    def send_jobs(self, jobs):
        for job in jobs[:10]:
            msg = (
                f"Decisão: {job.decision}\n"
                f"Score: {job.score}\n"
                f"Título: {job.title}\n"
                f"Empresa: {job.company}\n"
                f"Localização: {job.location}\n\n"
                f"{job.link}"
            )
            ok = self.send(msg)
            if not ok:
                logger.warning("Falha ao enviar vaga: %s", job.link)