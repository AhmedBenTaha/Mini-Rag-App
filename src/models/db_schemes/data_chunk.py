from pydantic import BaseModel,Field
from typing import Optional,Dict
from bson.objectid import ObjectId


class DataChunk(BaseModel):
    id:Optional[ObjectId]= Field(None,alias="_id")
    chunk_text: str  = Field(...,min_lenght=1)
    chunk_metadata:Dict
    chunk_order:int = Field(...,gt=0)
    chunk_project_id:ObjectId
    
    class Config:
        arbitrary_types_allowed = True
        
    @classmethod
    def get_indexes(cls):
        
        return [
            {
                "key":[("chunk_project_id",1)],
                "name":"chunk_project_id_index_1",
                "unique":False
            }
            
        ]    
        