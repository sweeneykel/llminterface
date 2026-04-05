# https://news.ycombinator.com/item?id=42095012
import sqlite3

def query_only_db(query_db_sql_command: str, db_name: str):
    # query (connect only with read only for query) But can write via the sqlite_db
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    try:
        # TODO: right now isn't read only, can write as well.
        cur.execute(query_db_sql_command)
    except Exception:
        raise
    conn.close()

def modify_sql_db(modify_db_sql_command: str, db_name: str):
    # will create this db if it does not exist
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()


    conn.close()