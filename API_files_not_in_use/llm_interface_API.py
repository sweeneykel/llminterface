from fastapi import FastAPI
from llm_interface_logic import translate_nsl_ql

app = FastAPI()

# called by Query Service
@app.get("/table/{table_name}")
async def GET(query):
    result = translate_nsl_ql(query)
    return result