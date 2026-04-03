import sqlite3

def create_new_table(passed_df):
    # con represents the connection to the on-disk database. Implicitly creates db if doesn't already exist. Create in cwd.
    con = sqlite3.connect("new_test_db")
    # in order to execute SQL statements and fetch results, use a database cursor
    cur = con.cursor()
    # create a db table with columns

    # LLM: If input is inserted into the SQL string → it can become a command
    # LLM: If input is passed via placeholders → it is always treated as data
    cur.execute("CREATE TABLE, params movie(title, year, score)")
    # test that this worked
    #res = cur.execute("SELECT name FROM sqlite_master")
    #print("result", res.fetchone())
    return 0

# append to existing table. Insert lines. (confirm that schemas are exact match!!)
def append_to_existing_table(passed_df):
    return 0