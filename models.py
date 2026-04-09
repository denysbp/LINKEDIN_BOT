from dataclasses import dataclass

@dataclass
class Job:
    title: str
    company: str
    location: str
    date: str
    link: str
    score: int = 0
    decision: str = ""