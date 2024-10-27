from fastapi import APIRouter

router = APIRouter()

@router.get("/users/1")
async def read_user():
    return {"user_id": 1, "message": f"Root user."}
@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "message": f"User with ID {user_id} found."}

@router.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id, "message": f"Item with ID {item_id} found."}
