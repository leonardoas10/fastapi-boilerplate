# app/routers/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_users():
    return {"message": "Read userss"}
