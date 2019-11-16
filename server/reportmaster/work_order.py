import json

from pydantic import BaseModel
from datetime import datetime

from reportmaster.worker import Worker


class WorkOrder(BaseModel):
    data: dict
    status: str = "new"
    category: str
    created: datetime = None
    modified: datetime = None
    id: int = 0
    hour_restrictions: str = None
    assigned_to: Worker = None

    def to_db(self):
        data = self.dict()
        data["data"] = str(json.dumps(data["data"]))
        return data

    @staticmethod
    def from_db(data):
        data["data"] = json.loads(data["data"])
        return WorkOrder(**data)
