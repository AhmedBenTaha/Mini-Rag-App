from fastapi import FastAPI
from src.routes import base
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(base.base_router)

