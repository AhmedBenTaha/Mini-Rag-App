from .BaseController import BaseController
from .ProcessController import ProcessController



class ProcessController(BaseController):
    def __init__(self,project_id:str):
        super().__init__()
        self.project_id = self.project_id