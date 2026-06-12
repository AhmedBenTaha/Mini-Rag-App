from fastapi import FastAPI,APIRouter,Depends
import os
from src.helpers.config import get_setting,settings

base_router = APIRouter(
    prefix='/api/v1',
    tags=['api-v1']
)

@base_router.get('/')
async def welcome(app_setting:settings = Depends(get_setting)):
    app_name = app_setting.app_name
    app_version = app_setting.app_version
    return{
        'App Name': app_name,
        'App Version': app_version
    }