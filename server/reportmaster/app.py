from datetime import datetime
from fastapi import FastAPI

from reportmaster.work_order import WorkOrder
from reportmaster.worker import Worker

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/project/")
def post_project(project: WorkOrder):
    return project


@app.get("/project/")
def get_project(id: int):
    worker = Worker(id=123, name="Teuvo Teräväinen")
    return WorkOrder(id=id, description="Description", created=datetime.now(), assigned_to=worker)

