from fastapi import FastAPI
from schema_manager_logic import append_or_create, find_schema_context

app = FastAPI()

#TODO: How does this become exposed only to the modules that can have access?

@app.get("/table/{table_name}")
async def GET_ACTION(table):
    result = append_or_create(table)
    return result

@app.get("/table/{table_name}")
async def GET_CONTEXT(table):
    result = find_schema_context(table)
    return result