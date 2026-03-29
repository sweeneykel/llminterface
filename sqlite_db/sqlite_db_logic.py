import sqlite3




# con represents the connection to the on-disk database
con = sqlite3.connect("tutorial.db")
# in order to execute SQL statements and fetch results, use a database cursor
cur = con.cursor()
# create a db table with columns
cur.execute("CREATE TABLE, params movie(title, year, score)")
# test that this worked
res = cur.execute("SELECT name FROM sqlite_master")
print("result", res.fetchone())


def create_new_table(user_submit):
    return 0
