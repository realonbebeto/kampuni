from sqlalchemy.orm import Session
from models.entities.entities import Department
from fastapi import HTTPException, status

def getAll(db: Session):
    departments = db.query(Department).all()
    return departments

def createDepartment(request: Department, db: Session):
    newDepartmentModel = Department(name=request.name)
    db.add(newDepartmentModel)
    db.commit()
    db.refresh(newDepartmentModel)
    return newDepartmentModel

def deleteDepartmentByID(id: int, db: Session):
    department = db.query(Department).filter(Department.id == id)

    if not department.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Department with id {id} not found')

    department.delete(synchronize_session=False)
    db.commit()
    return 'done'

def updateDepartmentByID(id: int, request: Department, db: Session):
    department = db.query(Department).filter(Department.id == id)

    if not department.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Department with id {id} not found')

    department.update(request)
    db.commit()
    return 'updated'

def getDepartmentByID(id: int, db: Session):
    department = db.query(Department).filter(Department.id == id)

    if not department.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Department with id {id} not found')
    
    return department

