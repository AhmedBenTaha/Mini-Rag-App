from typing import Optional
from pydantic import BaseModel,Field,validator
from bson.objectid import ObjectID


class Project(BaseModel):
    _id : Optional[ObjectID]
    project_id:str = Field(...,min_lenght=1)
    
    @validator('project_id')
    def validate_project_id(cls,value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value
    
    class config:
        arbitrary_types_allowed = True