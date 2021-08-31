from fastapi import APIRouter, Depends, status
from database import getToDb
from v1.reposervices import EmployeeRepo
from models.response import HTTPResponse
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/employee",
    tags=['Employees']
)

get_db = getToDb

@router.get('/', response_model=List[HTTPResponse.ShowEmployee])
def getAll(db: Session = Depends(get_db)):
    return EmployeeRepo.getAll(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def createEmployee(request: HTTPResponse.Employee, db: Session = Depends(get_db)):
    return EmployeeRepo.createEmployee(db, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteEmployeeById(id:int, db: Session = Depends(get_db)):
    return EmployeeRepo.deleteEmployeeByID(id, db)

@router.put('/', status_code = status.HTTP_202_ACCEPTED)
def updateEmployeeById(id:int, request: HTTPResponse.Employee, db: Session = Depends(get_db)):
    return EmployeeRepo.updateEmployeeByID(id, db, request)

@router.get('/{id}', status_code = status.HTTP_200_OK)
def getEmployeeById(id:int, db: Session = Depends(get_db)):
    return EmployeeRepo.getEmployeeByID(id, db)