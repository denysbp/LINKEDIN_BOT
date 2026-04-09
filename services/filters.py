import logging

logger = logging.getLogger(__name__)

class SmartFilter:
    def filter(self, jobs: list):
        """Filtra lista de vagas para júnior backend reais."""
        if not jobs:
            return []
        return [job for job in jobs if self.is_real_junior(job) and self.is_backend(job)]

    def is_real_junior(self, job):
        title = (job.title or "").lower()

        fake_patterns = [
            "senior",
            "sr ",
            "lead",
            "principal",
            "5+",
            "4+",
            "3+ years",
            "architect"
        ]

        junior_patterns = [
            "junior",
            "jr",
            "entry",
            "trainee",
            "graduate",
            "intern"
        ]

        if any(x in title for x in fake_patterns):
            return False

        return any(x in title for x in junior_patterns)

    def is_backend(self, job):
        text = ((job.title or "") + " " + (getattr(job, "company", "") or "")).lower()
        keywords = ["backend", "python", "java", "spring", "api"]
        return any(k in text for k in keywords)

    def score(self, job):
        score = 0
        title = (job.title or "").lower()

        if "python" in title:
            score += 3
        if "java" in title:
            score += 3
        if "backend" in title:
            score += 2
        if "spring" in title:
            score += 2
        if "junior" in title:
            score += 1

        return score