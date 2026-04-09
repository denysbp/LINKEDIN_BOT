import os
from flask import Flask, render_template_string, make_response
from logging_config import configure_logging

configure_logging(os.getenv("LOG_LEVEL", "INFO"))

from services.linkedin import LinkedInClient
from services.parser import Parser
from services.filters import SmartFilter
from config import KEYWORDS, LOCATION
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def home():
    try:
        client = LinkedInClient()
        parser = Parser()
        flt = SmartFilter()

        html = client.fetch(KEYWORDS, LOCATION)
        jobs = parser.parse(html)
        jobs = flt.filter(jobs)

        template = """
        <h1>Vagas Backend Junior</h1>
        {% for job in jobs %}
            <div>
                <h3>{{job.title}}</h3>
                <p>{{job.company}} - {{job.location}}</p>
                <a href="{{job.link}}">Ver vaga</a>
                <hr>
            </div>
        {% endfor %}
        """

        return render_template_string(template, jobs=jobs)
    except Exception as e:
        logger.exception("Erro ao gerar página inicial: %s", e)
        return make_response("Erro interno", 500)


if __name__ == "__main__":
    app.run(host=os.getenv("FLASK_HOST", "0.0.0.0"), port=int(os.getenv("FLASK_PORT", 5000)), debug=(os.getenv("FLASK_DEBUG") == "1"))