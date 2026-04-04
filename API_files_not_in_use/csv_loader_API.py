# ChatGPT Source: Project Structure

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from logic_main.csv_loader_logic import upload_data

app = FastAPI()

class TableInput(BaseModel):
    table_path: str

# ChatGPT Source: code review #1: https://chatgpt.com/g/g-p-69c84b135ed48191b95908e323c125fd-ec530-llm-interface-project/project?tab=sources
# @app.post("/table")
# TODO: blocking call inside async route
def add_table(request: TableInput):
    try:
        result = upload_data(request.table_path)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))