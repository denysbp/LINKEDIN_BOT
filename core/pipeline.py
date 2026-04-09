from database import is_sent, mark_as_sent
from services.filters import SmartFilter
from services.scoring import JobScorer, DecisionEngine
import logging

logger = logging.getLogger(__name__)

flt = SmartFilter()
scorer = JobScorer()
decider = DecisionEngine()


def process_jobs(jobs, notifier):
    new_jobs = []

    for job in jobs:

        if not flt.is_real_junior(job):
            continue

        if not flt.is_backend(job):
            continue

        if is_sent(job.link):
            continue

        score = scorer.score(job)
        decision = decider.decide(score)

        job.score = score
        job.decision = decision

        new_jobs.append(job)
        mark_as_sent(job)

    new_jobs.sort(key=lambda x: x.score, reverse=True)

    try:
        notifier.send_jobs(new_jobs)
        logger.info("Notificadas %d vagas", len(new_jobs))
    except Exception:
        logger.exception("Falha ao notificar vagas")