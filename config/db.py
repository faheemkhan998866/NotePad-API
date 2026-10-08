import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# LOCAL MongoDB Server only. Compass is NOT required.
MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "inotes")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000,
)
db = client[MONGO_DB_NAME]
notes_collection = db["notes"]


def check_database() -> bool:
    """Return True when the local MongoDB server is reachable."""
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False
