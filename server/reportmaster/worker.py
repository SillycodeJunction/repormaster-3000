from pydantic import BaseModel


class Worker(BaseModel):
    id: int
    name: str
    projects: list = None
