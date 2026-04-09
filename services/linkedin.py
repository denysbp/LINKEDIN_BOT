import requests

BASE_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"

class LinkedInClient:
    def __init__(self):
        self.session = requests.Session()

    def fetch(self, keywords, location, start=0):
        params = {
            "keywords": keywords,
            "location": location,
            "start": start,
        }
        res = self.session.get(BASE_URL, params=params)
        res.raise_for_status()
        return res.text