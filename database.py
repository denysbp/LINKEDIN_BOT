import sqlite3
from contextlib import closing
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME_ENV")


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS sent_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT UNIQUE,
                title TEXT,
                company TEXT,
                date_sent TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def is_sent(link: str) -> bool:
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT 1 FROM sent_jobs WHERE link = ?", (link,))
        result = c.fetchone()
        return result is not None


def mark_as_sent(job):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("""
            INSERT OR IGNORE INTO sent_jobs (link, title, company)
            VALUES (?, ?, ?)
        """, (getattr(job, "link", None), getattr(job, "title", None), getattr(job, "company", None)))
        conn.commit()