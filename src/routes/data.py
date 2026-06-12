from fastapi import FastAPI,APIRouter,Depends,UploadFile
import os
from helpers.config import get_setting,settings
from controllers import DataController


data_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api-v1','data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str,file:UploadFile,
                      app_setting:settings = Depends(get_setting)):
    
    is_valid = DataController().validate_uploaded_file(file)
    
    return is_valid
    