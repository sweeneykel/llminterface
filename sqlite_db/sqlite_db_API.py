from fastapi import FastAPI
from sqlite_db_logic import add_new_table, append_to_table, get_query

app = FastAPI()

# called by Schema Manager, Query Service
@app.post("/table/{table_name}")
async def POST_TABLE(query):
    result = add_new_table(query)
    return result

@app.put("/table/{table_name}")
async def APPEND_TABLE(query):
    result = append_to_table(query)
    return result

@app.get("/table/{table_name}")
async def GET_QUERY(query):
    result = get_query(query)
    return result