from fastapi import FastAPI
from src.routes import base
from src.routes import data
from src.helpers.config import get_setting
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

@app.on_event('startup')
async def startup_db_client():
    setting = get_setting()
    app.mongo_conn = AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client = app.mongo_conn[setting.MONGODB_DATABASE]

@app.on_event('shutdown')
async def shutdown_db_client():
    app.mongo_conn.close()

app.include_router(base.base_router)

app.include_router(data.data_router)
