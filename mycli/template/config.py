import os
from dotenv import load_dotenv

load_dotenv()

def get_env(key, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        raise ValueError(f"Missing required env variable: {key}")
    return value

DB_CONFIG = {
    "host": get_env("DB_HOST", required=True),
    "user": get_env("DB_USER", required=True),
    "password": get_env("DB_PASSWORD", required=True),
    "database": get_env("DB_NAME", required=True),
}

FOLDER_PATH = get_env("INPUT_FOLDER", required=True)
OUTPUT_FOLDER_PATH = get_env("OUTPUT_FOLDER", "./output")

MAX_WORKERS = int(get_env("MAX_WORKERS", 5))
BATCH_SIZE = int(get_env("BATCH_SIZE", 500))