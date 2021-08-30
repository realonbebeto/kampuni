from fastapi import FastAPI
from database import engine
from models.entities import entities
from v1.controllers import EmployeeController, DepartmentController

app =FastAPI()

entities.Base.metadata.create_all(engine)

app.include_router(EmployeeController.router)
app.include_router(DepartmentController.router)