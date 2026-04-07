import mysql.connector
from config import DB_CONFIG
from logger import setup_logger

logger = setup_logger()

def get_connection():
    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )

def get_connection_thread():
    return mysql.connector.connect(**DB_CONFIG)

def create_database(cursor):
    db_name = DB_CONFIG["database"]
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.execute(f"USE {db_name}")
    logger.info(f"Database ready: {db_name}")

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_name(
        id INT AUTO_INCREMENT PRIMARY KEY
    )
    """)
    logger.info("Table created")

def insert_multiple_data(cursor, data):
    if not data:
        return

    query = "INSERT INTO table_name() VALUES ()"
    cursor.executemany(query)
    logger.info(f"Inserted {len(data)} records")