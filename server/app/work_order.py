import json

from pydantic import BaseModel
from datetime import datetime

from app.worker import Worker


class WorkOrder(BaseModel):
    data: dict
    status: str = "new"
    owner_id: str = None
    category: str
    created: datetime = None
    modified: datetime = None
    id: int = 0
    hour_restrictions: str = None
    assigned_to: Worker = None

    def to_db(self):
        data = self.dict()
        data["data"] = str(json.dumps(data["data"]))
        data["worker_id"] = self.assigned_to.id if self.assigned_to else 0
        return data

    @staticmethod
    def from_db(data, worker=None):
        data["data"] = json.loads(data["data"])
        data["assigned_to"] = worker
        return WorkOrder(**data)
