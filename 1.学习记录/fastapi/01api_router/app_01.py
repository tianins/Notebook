from fastapi import APIRouter

router_user = APIRouter()

@router_user.get("/user")
async def get_users():
    return [{"username": "user1"}, {"username": "user2"}]

@router_user.post("/user")
async def create_user(user: dict):
    return {"message": "User created", "user": user}
