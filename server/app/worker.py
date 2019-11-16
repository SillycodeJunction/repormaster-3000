from pydantic import BaseModel


class Worker(BaseModel):
    id: int = 0
    name: str
    role: str
    projects: list = None
