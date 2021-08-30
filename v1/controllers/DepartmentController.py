from fastapi import APIRouter, Depends, status
from database import getToDb
from v1.reposervices import DepartmentRepo
from models.response import HTTPResponse
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/deparment",
    tags = ['Departments']
)

get_db = getToDb

@router.get('/', response_model = List[HTTPResponse.ShowDepartment], status_code=status.HTTP_200_OK)
def getAll(db: Session = Depends(get_db)):
    return DepartmentRepo.getAll(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def createDepartment(request: HTTPResponse.Department, db: Session = Depends(get_db)):
    return DepartmentRepo.createDepartment(request, db)

@router.delete('/{id}', status_code =status.HTTP_204_NO_CONTENT)
def deleteDepartmentByID(id:int, db: Session = Depends(get_db)):
    return DepartmentRepo.deleteDepartmentByID(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateDepartmentById(id:int, request: HTTPResponse.Department, db: Session = Depends(get_db)):
    return DepartmentRepo.updateDepartmentByID(id,request,db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model= HTTPResponse.ShowDepartment)
def getDepartmentByID(id:int, db: Session = Depends(get_db)):
    return DepartmentRepo.getDepartmentByID(id, db)
