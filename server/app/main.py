import app.db as db

from fastapi import FastAPI

from app.work_order import WorkOrder
from app.worker import Worker

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/workorder/list/")
def list_workorders(owner: str):
    return db.get_work_orders_by_owner(owner)


@app.post("/workorder/")
def post_project(work_order: WorkOrder):
    id = db.create_work_order(work_order)
    created_order = db.get_work_order_by_id(id)
    return created_order


@app.get("/workorder/")
def get_project(id: int):
    return db.get_work_order_by_id(id)


@app.put("/workorder/update/")
def edit_project(id: int, data: dict = None, status: str = None):
    work_order = db.get_work_order_by_id(id)
    if data:
        work_order.data = data
        db.update_work_order_data(work_order)
    if status:
        work_order.status = status
        db.update_work_order_status(work_order)

    return db.get_work_order_by_id(id)


@app.put("/workorder/assign")
def assign_worker(id: int, workerId: int):
    return db.assign_worker(order_id=id, worker_id=workerId)


@app.post("/worker/")
def add_worker(worker: Worker):
    id = db.add_worker(worker)
    return db.get_worker_by_id(id)
