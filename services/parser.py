from bs4 import BeautifulSoup
from models import Job
import logging

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
        )

    def _get_text(self, card, selector: str) -> str:
        el = card.select_one(selector)
        return el.get_text(strip=True) if el else ""

    def _get_attr(self, card, selector: str, attr: str) -> str:
        el = card.select_one(selector)
        return el.get(attr, "") if el else ""