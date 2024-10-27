from fastapi import FastAPI, APIRouter
from apps import app_01,app_02,app_03

app = FastAPI()

app.include_router(app_01.router, prefix="/api/v1",tags=['路径参数'])
app.include_router(app_02.router, prefix="/api/v2",tags=['查询参数'])
app.include_router(app_03.router, prefix="/api/v3",tags=['请求体数据'])


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("mian:app", host="127.0.0.1", port=8010, reload=True)