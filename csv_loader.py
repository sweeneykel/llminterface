from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# fastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs
# http://127.0.0.1:8000/docs

#baseURL = 'http://127.0.0.1:8000'

#{"id":
#     {
#         "name": name,
#         "description": description,
#         "completed": bool,
#         "start_date": start_date,
#         "start_time": start_time,
#         "end_date": end_date,
#         "end_time": end_time,
#     }
# }

#TODO: here it is a single field start_datetime but in SQLite it is two fields
task_fields = [
    "name",
    "description",
    "completed",
    "start_datetime",
    "end_datetime",
]
first_task = [
    "long run",
    "go for a 60 minute run",
    False,
    datetime(2026, 2, 21, 8, 30),
    datetime(2026, 2, 21, 10, 30)
]

task_dict = {
    1: dict(zip(task_fields, first_task))
}

task_id_MASTER = 1

# create task in database
@app.post("/tasks/{task_id}")
async def make_task(name:str, description:str, completed:bool, start_datetime:datetime, end_datetime:datetime):
    task_id = task_id_MASTER + 1
    task_dict[task_id] = {"name": name,
                          "description": description,
                          "completed": completed,
                          "start_datetime": start_datetime,
                          "end_datetime": end_datetime
                          }
    return task_dict[task_id]