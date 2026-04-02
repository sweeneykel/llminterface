from fastapi import FastAPI
from sql_db_validator_logic import validate_LLM_output

app = FastAPI()

# called by Query Service
@app.get("/table/{table_name}")
async def VALIDATE(table):
    result = validate_LLM_output(table)
    return result