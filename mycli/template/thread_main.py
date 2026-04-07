import os
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

from parser import parse_file
from db import get_connection, get_connection_thread, create_table, create_database, insert_multiple_data
from config import FOLDER_PATH, BATCH_SIZE, MAX_WORKERS
from logger import setup_logger

logger = setup_logger()

def insert_batch(batch):
    conn = get_connection_thread()
    cursor = conn.cursor()

    insert_multiple_data(cursor, batch)
    conn.commit()

    cursor.close()
    conn.close()

def main():
    start = time.time()

    conn = get_connection()
    cursor = conn.cursor()
    create_database(cursor)
    create_table(cursor)
    conn.commit()
    cursor.close()
    conn.close()

    batch = []
    futures = []

    with ThreadPoolExecutor(MAX_WORKERS) as parser_pool:
        tasks = {
            parser_pool.submit(parse_file, os.path.join(FOLDER_PATH, f)): f
            for f in os.listdir(FOLDER_PATH)
        }

        with ThreadPoolExecutor(MAX_WORKERS) as db_pool:
            for future in as_completed(tasks):
                result = future.result()

                if result:
                    batch.append(result)

                if len(batch) >= BATCH_SIZE:
                    futures.append(db_pool.submit(insert_batch, batch.copy()))
                    batch.clear()

            if batch:
                futures.append(db_pool.submit(insert_batch, batch.copy()))

            for f in futures:
                f.result()

    logger.info(f"Runtime: {time.time() - start}")