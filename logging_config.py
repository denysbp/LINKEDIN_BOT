import logging
import os
from logging.handlers import RotatingFileHandler


def configure_logging(level: str = "INFO", log_file: str = "logs/bot.log"):
    """Configura logging básico com handler de console e arquivo rotativo.

    level: nível de logging (DEBUG/INFO/WARNING/ERROR)
    log_file: caminho para arquivo de logs
    """
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(level=numeric_level,
                        format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
    try:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        fh = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=3)
        fh.setLevel(numeric_level)
        fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s"))
        logging.getLogger().addHandler(fh)
    except Exception:
        logging.getLogger(__name__).exception("Não foi possível criar handler de arquivo de logs")
