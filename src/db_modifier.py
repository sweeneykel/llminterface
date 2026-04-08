# https://news.ycombinator.com/item?id=42095012
import sqlite3
import pandas as pd


# TODO: right now isn't read only, can write as well.
def query_only_db(query_db_sql_command: str, db_name: str):
    # query (connect only with read only for query) But can write via the sqlite_db
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    try:
        db_response = cur.execute(query_db_sql_command).fetchone()
    except Exception as e:
        raise

    conn.close()
    print("db_modifier.py", db_response)

    return db_response

def modify_sql_add_table(modify_db_sql_command: str, df: pd.DataFrame,  db_name: str, table_name: str):
    # will create this db if it does not exist
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    print("This is the SQL command that will be used to create a new table.")
    print("*********")
    print(modify_db_sql_command)
    print("*********")
    user_choice = input(" Do you want to proceed with this command? Type CONFIRM"
                        " to proceed. Type any other letter to cancel this process.").strip()
    if user_choice == "CONFIRM":
        cur.execute(modify_db_sql_command)
        res = cur.execute(f"SELECT name FROM sqlite_master WHERE name='{table_name}'")
        # If a table called table_name was not created, then this line will NOT execute
        if res.fetchone() is not None:
            print('hi')

    conn.close()
