import os
from parser import parse_file
from db import FOLDER_PATH, get_connection, create_table, insert_data, create_database
from logger import setup_logger

logger = setup_logger()
def main():
    conn = get_connection()
    cursor = conn.cursor()
    
    create_database(cursor)
    create_table(cursor)
    
    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)
        print(f"Processing: {file_name}")

        try:
            data = parse_file(file_path)
            insert_data(cursor,data)
            conn.commit()

        except Exception as e:
            print(f"Error in {file_name}: {e}")

    cursor.close()
    conn.close()
    print("Done!")

if __name__ == "__main__":
    main()