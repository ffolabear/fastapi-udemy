from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Users
from routers.auth import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['user'],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/")
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed.')
    login_user = db.query(Users).filter(Users.id == user.get("id")).first()
    if login_user is None:
        raise HTTPException(status_code=404, detail="Invalid user.")
    return user


@router.post("/{user_id}")
async def change_password(user: user_dependency, password: str, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed.')
    user = db.query(Users).filter(Users.id == user.get("id")).first()
    user.password = password
    db.add(user)
    db.commit()
