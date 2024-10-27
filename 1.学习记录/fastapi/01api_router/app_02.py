from fastapi import APIRouter

router_item = APIRouter()

@router_item.get("/item")
async def get_items():
    return [{"item": "Item 1"}, {"item": "Item 2"}]

@router_item.post("/item")
async def create_item(item: dict):
    return {"message": "Item created", "item": item}
