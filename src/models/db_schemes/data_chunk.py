from pydantic import BaseModel,Field
from typing import Optional,Dict
from bson.objectid import ObjectId


class DataChunk:
    _id:Optional[ObjectId]
    chunk_text: str  = Field(...,min_lenght=1)
    chunk_metadata:Dict
    chunk_order:int = Field(...,gt=0)
    chunk_project_id:ObjectId
    
    class config:
        arbitrary_types_allowed = True