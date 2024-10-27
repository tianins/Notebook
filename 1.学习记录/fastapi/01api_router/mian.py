from fastapi import FastAPI, APIRouter
from app_01 import router_user
from app_02 import router_item
app = FastAPI()

app.include_router(router_user, prefix="/api/v1",tags=['用户'])
app.include_router(router_item, prefix="/api/v1",tags=['商品'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)