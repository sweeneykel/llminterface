from fastapi import FastAPI
from pydantic import BaseModel
from sqlite_db_logic import create_new_table, append_to_table, get_query

class TableClass(BaseModel):
    table_name: str



app = FastAPI()

# Creates a new table when there is no existing matching schema
@app.post("/table")
async def create_table(user_submit: TableClass):
    result = create_new_table(user_submit)
    return result

# Appends uploaded data to an existing table when there is a matching schema
@app.put("/db/{table_name}")
async def append_table(query):
    result = append_to_table(query)
    return result

# Finds appropriate table and retrieves requested information
@app.get("/db/{table_name}")
async def GET_QUERY(query):
    result = get_query(query)
    return result