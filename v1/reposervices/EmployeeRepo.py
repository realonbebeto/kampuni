from sqlalchemy.orm import Session
from models.entities.entities import Employee
from v1.reposervices.DepartmentRepo import getDepartmentByID
from fastapi import HTTPException, status

def getAll(db: Session):
    employees = db.query(Employee).all()
    return employees


def createEmployee(db: Session, request: Employee):

    newEmployeeModel = Employee(firstName=request.firstName, middleName=request.midName, lastName=request.lastName, email=request.email, department=request.department)
    db.add(newEmployeeModel)
    db.commit()
    db.refresh(newEmployeeModel)

def deleteEmployeeByID(id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == id)

    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Employee of id {id} not found')
    
    employee.delete(synchronize_session=False)
    employee.commit()
    return 'done'

def updateEmployeeByID(id: int, db: Session, request:Employee):
    employee = db.query(Employee).filter(Employee.id == id)

    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Employee of id {id} not found')

    db.update(request)
    db.commit()

    return 'updated'

def getEmployeeByID(id:int, db:Session):
    employee = db.query(Employee).filter(Employee.id == id)

    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Employee of id {id} not found')

    return employee