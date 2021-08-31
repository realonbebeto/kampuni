from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    midName = Column(String)
    lastName = Column(String)
    email = Column(String, unique=True)

    department_id = Column(Integer, ForeignKey('departments.id'))

    owner = relationship('Department', back_populates='employees')

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    employees = relationship('Employee', back_populates='owner')