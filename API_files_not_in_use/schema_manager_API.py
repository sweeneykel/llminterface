from fastapi import FastAPI
from src.schema_manager import append_or_create, find_schema_context

app = FastAPI()

# called by CSV Ingestor, Query Service
@app.get("/table/{table_name}")
async def GET_ACTION(table):
    result = append_or_create(table)
    return result

@app.get("/table/{table_name}")
async def GET_CONTEXT(table):
    result = find_schema_context(table)
    return result