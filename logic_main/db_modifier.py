# https://news.ycombinator.com/item?id=42095012
import sqlite3

def query_only_db(query_db_sql_command: str, db_name: str):
    # query (connect only with read only for query) But can write via the sqlite_db
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    try:
        # TODO: right now isn't read only, can write as well.
        db_response = cur.execute(query_db_sql_command).fetchone()

    except Exception as e:
        raise

    conn.close()
    print("db_modifier.py", db_response)

    return db_response

def modify_sql_add_table(modify_db_sql_command: str, db_name: str, table_name: str):
    # will create this db if it does not exist
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    print("This is the SQL command that will be used to create a new table.")
    print("*********")
    print(modify_db_sql_command)
    print("*********")
    user_choice = input(" Do you want to proceed with this command? Type CONFIRM COMMAND"
                        " to proceed. Type any other letter to cancel this process.").strip()

    if user_choice == "CONFIRM COMMAND":
        cur.execute(modify_db_sql_command)

    res = cur.execute("SELECT name FROM sqlite_master WHERE name='",table_name,"')")
    conn.close()
