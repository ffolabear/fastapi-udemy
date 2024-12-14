from fastapi import FastAPI
import models
from database import engine
from project3.TodoApp.database import SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()