from fastapi import FastAPI,APIRouter
from typing import Optional

router = APIRouter()

@router.get("/items/")
async def read_items(skip: Optional[int] = 0, limit: Optional[int] = 10):
    return {"skip": skip, "limit": limit, "items": ["item1", "item2", "item3"]}

@router.get("/users/")
async def read_users(age: Optional[int] = None, city: Optional[str] = None):
    return {
        "age": age,
        "city": city,
        "message": "User data retrieved successfully."
    }