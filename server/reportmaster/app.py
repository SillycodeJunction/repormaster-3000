from fastapi import FastAPI

from reportmaster.project import Project

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/project/")
def post_project(project: Project):
    return project


@app.get("/project/")
def get_project(id: int):
    return Project(id=id, description="Description")

