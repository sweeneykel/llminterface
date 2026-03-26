from fastapi import FastAPI
from query_service_logic import *

app = FastAPI()

# POST
@app.get("/table/{table_name}")
async def GET(query):
    result = get_query(query)
    return result