from pydantic import BaseModel


class Project(BaseModel):
    description: str
    status: str = "new"
    id: int = 0
