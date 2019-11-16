import reportmaster.db as db

from fastapi import FastAPI

from reportmaster.work_order import WorkOrder
from reportmaster.worker import Worker

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/workorder/")
def post_project(work_order: WorkOrder):
    id = db.create_work_order(work_order)
    created_order = db.get_work_order_by_id(id)
    return created_order


@app.get("/workorder/")
def get_project(id: int):
    return db.get_work_order_by_id(id)


@app.put("/workorder/updateData/")
def edit_project(id: int, data: dict):
    worker = db.get_work_order_by_id(id)
    worker.data = data

    return worker


@app.put("/workorder/assign")
def assign_worker(id: int, workerId: int):
    return db.assign_worker(order_id=id, worker_id=workerId)


@app.post("/worker/")
def add_worker(worker: Worker):
    id = db.add_worker(worker)
    return db.get_worker_by_id(id)
