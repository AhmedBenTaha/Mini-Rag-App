from .BaseController import BaseController
from fastapi import UploadFile
from src.models.enums import ResponseStatus

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024 # Convert bytes to MB
        
    def validate_uploaded_file(self, file:UploadFile):
            
            if file.content_type not in self.app_setting.FILE_ALLOWED_TYPES:
                return False, ResponseStatus.FILE_TYPE_NOT_SUPPORTED.value
            if file.size > self.app_setting.MAX_FILE_SIZE * self.size_scale:
                return False , ResponseStatus.FILE_SIZE_EXCEEDED.value
            
            return True , ResponseStatus.FILE_VALIDATED_SUCCESS.value