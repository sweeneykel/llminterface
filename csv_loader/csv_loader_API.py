# structure guidance from ChatGPT
# https://chatgpt.com/s/t_69c52dff34ac81918290c060b6daba5a

from fastapi import FastAPI
from csv_loader_logic import add_new_table

app = FastAPI()

# POST
@app.post("/table/{table_name}")
async def POST_TABLE(table):
    result = add_new_table(table)
    return result