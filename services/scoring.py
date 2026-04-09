class JobScorer:
    def score(self, job):
        score = 0
        title = job.title.lower()

        if "python" in title:
            score += 3
        if "java" in title:
            score += 3
        if "backend" in title:
            score += 2
        if "junior" in title:
            score += 3

        if "portugal" in job.location.lower():
            score += 1

        if any(x in title for x in ["senior", "lead"]):
            score -= 5

        if any(x in title for x in ["bootcamp", "trainee"]):
            score -= 1

        return score


class DecisionEngine:
    def decide(self, score):
        if score >= 7:
            return "Vale muito a pena aplicar"
        elif score >= 4:
            return "Vale a pena aplicar"
        else:
            return "Melhor ignorar"