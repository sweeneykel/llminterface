from fastapi import FastAPI
from query_service_logic import get_query

app = FastAPI()

# POST
# TODO: i'm not sure if the URL is needed. I think I need to reference the SQLite db.
@app.get("/table/{table_name}")
async def GET(query):
    result = get_query(query)
    return result