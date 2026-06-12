from .BaseController import BaseController
from fastapi import UploadFile
from src.models.enums import ResponseStatus



class ProjectController(BaseController):
    def __init__(self):
        super().__init__()