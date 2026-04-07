import json
import gzip
import os
from logger import setup_logger
from header import get_headers

logger = setup_logger()

def load_file(file_path):
    name, ext = os.path.splitext(file_path)

    try:
        if ext == ".gz":
            with gzip.open(file_path, "rt", encoding="utf-8") as f:
                return json.load(f)

        elif ext == ".json":
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)

        else:
            logger.warning(f"Unsupported file: {file_path}")
            return None

    except Exception as e:
        logger.error(f"File read error: {file_path} | {e}")
        return None


# MAIN PARSER ENTRY
def parse_file(file_path):
    raw = load_file(file_path)
    if not raw:
        return None

    try:
        return transform(raw)
    except Exception as e:
        logger.error(f"Parse error: {file_path} | {e}")
        return None

def transform(raw):
    """
    User writes extraction logic here
    Supports:
    - JSON
    - lxml
    - parsel
    """
    return raw