from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

SQL_DATABASE_URL = 'sqlite:///kampuni.db'

engine  = create_engine(SQL_DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def getToDb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()