from typing import List, Optional
from pydantic import BaseModel


class EmployeeBase(BaseModel):
    firstName: str
    midName: str = None
    lastName: str
    email: str
    department: int

class Employee(EmployeeBase):
    class Config():
        orm_mode = True

class Department(BaseModel):
    name: str

class ShowDepartment(BaseModel):
    name: str
    employees: List[Employee] = None

    class Config():
        orm_mode = True

class ShowEmployee(BaseModel):
    firstName: str
    midName: str
    lastName: str
    email: str
    department: ShowDepartment

    class Config():
        orm_mode = True