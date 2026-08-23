from bs4 import BeautifulSoup
from models import Job
import logging
from config import KEYWORDS

logger = logging.getLogger(__name__)

class Parser:
    def parse(self, html: str) -> list[Job]:
        soup = BeautifulSoup(html, "html.parser")

        jobs: list[Job] = []

        for card in soup.select(".base-card"):
            job = self._parse_card(card)
            if job:
                jobs.append(job)

        return jobs

    def _parse_card(self, card) -> Job | None:
        title = self._get_text(card, ".base-search-card__title")
        job_type = self._get_type(title)
        company = self._get_text(card, ".base-search-card__subtitle")
        location = self._get_text(card, ".job-search-card__location")
        date = self._get_attr(card, "time", "datetime")
        link = self._get_attr(card, "a", "href")

        if not title:
            logger.warning("Card sem título ignorado")
            return None
        if not link:
            return None

        if link.startswith("/"):
            link = "https://www.linkedin.com" + link

        return Job(
            title=title,
            company=company,
            location=location,
            date=date,
            link=link,
            type=job_type
        )

    def _get_type(self, title: str):
        title_list = title.lower().split(" ")
        title_dict  = {
            job: job for job in title_list
        }
        for job in KEYWORDS.lower().split(" "):
            if job not in title_list:
                continue
            job = title_dict.get(job, "unknown")
            if job in ("machine", "learning"):
                return "Machine Learning"
            if job in ("artificial", "intelligence"):
                return "AI"

            return job.capitalize()
        return "unknown"

    def _get_text(self, card, selector: str) -> str:
        el = card.select_one(selector)
        return el.get_text(strip=True) if el else ""

    def _get_attr(self, card, selector: str, attr: str) -> str:
        el = card.select_one(selector)
        return el.get(attr, "") if el else ""