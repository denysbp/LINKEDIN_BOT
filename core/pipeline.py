from database import is_sent, mark_as_sent
from services.filters import SmartFilter
from services.scoring import JobScorer, DecisionEngine
from services.notifier import TelegramNotifier
import logging

logger = logging.getLogger(__name__)

flt = SmartFilter()
scorer = JobScorer()
decider = DecisionEngine()


def process_jobs(jobs, notifier: TelegramNotifier):
    new_jobs = []
    for job in jobs:

        if not flt.valid_jobs(job):
            continue

        if is_sent(job.link):
            continue

        score = scorer.score(job)
        decision = decider.decide(score)

        job.score = score
        job.decision = decision

        new_jobs.append(job)

    if not new_jobs:
        logger.info("Nenhuma vaga nova para notificar")
        return
    new_jobs.sort(key=lambda x: x.score, reverse=True)

    try:
        notifier.send_jobs(new_jobs)
        for job in jobs:
            mark_as_sent(job)
        logger.info("Notificadas %d vagas", len(new_jobs))
    except Exception:
        logger.exception("Falha ao notificar vagas")