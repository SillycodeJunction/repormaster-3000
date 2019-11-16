from pydantic import BaseModel
from datetime import datetime

from reportmaster.worker import Worker


class WorkOrder(BaseModel):
    description: str
    status: str = "new"
    created: datetime = None
    id: int = 0
    hour_restrictions: str = None
    images: list = None
    assigned_to: Worker = None
