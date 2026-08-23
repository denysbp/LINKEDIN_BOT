import os
from flask import Flask, render_template_string, make_response, request
from logging_config import configure_logging
from dotenv import load_dotenv
from config import ensure_telegram_configured

ensure_telegram_configured()
configure_logging(os.getenv("LOG_LEVEL", "INFO"))
load_dotenv()

from services.linkedin import LinkedInClient
from services.parser import Parser
from services.filters import SmartFilter
from config import KEYWORDS, LOCATION
import logging

logger = logging.getLogger(__name__)

FILE = os.getcwd() + "/web/templates/index.html"

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
    )


@app.route("/")
def home():
    try:
        client = LinkedInClient()
        parser = Parser()
        flt = SmartFilter()
        PAGE_SIZE = 10
        page = request.args.get("page", 0, type=int)

        start = page * PAGE_SIZE
        html = client.fetch(KEYWORDS, LOCATION, start=start)
        jobs = parser.parse(html)
        jobs = flt.filter(jobs)


        file = open(FILE, "r")
        template = file.read()
        file.close()

        return render_template_string(template, jobs=jobs, page=page)
    except Exception as e:
        logger.exception("Erro ao gerar página inicial: %s", e)
        return make_response("Erro interno", 500)


if __name__ == "__main__":
    app.run(host=os.getenv("FLASK_HOST", "0.0.0.0"), port=int(os.getenv("FLASK_PORT", 5000)), debug=(os.getenv("FLASK_DEBUG") == "1"))