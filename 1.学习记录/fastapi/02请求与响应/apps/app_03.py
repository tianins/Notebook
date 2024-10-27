from fastapi import FastAPI,APIRouter
from pydantic import BaseModel

router = APIRouter()

# 定义数据模型
class Item(BaseModel):
    name: str
    description: str = None  # 可选字段
    price: float
    tax: float = None  # 可选字段

@router.post("/items/")
async def create_item(item: Item):
    return {
        "item_name": item.name,
        "item_description": item.description,
        "item_price": item.price,
        "item_tax": item.tax,
    }

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "item_name": item.name,
        "item_description": item.description,
        "item_price": item.price,
        "item_tax": item.tax,
    }
