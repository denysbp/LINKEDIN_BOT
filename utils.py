import json
import os

FILE = "sent_jobs.json"

def load_sent():
    if not os.path.exists(FILE):
        return set()
    return set(json.load(open(FILE)))

def save_sent(sent):
    json.dump(list(sent), open(FILE, "w"))