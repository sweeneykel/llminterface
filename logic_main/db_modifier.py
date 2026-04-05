# https://news.ycombinator.com/item?id=42095012
import sqlite3

def add_table_to_db(create_table_tablename: str, db_name: str):
    # will create this db if it does not exist
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute(create_table_tablename)

    conn.close()