from pydantic import BaseModel, Field
from typing import Optional



class PushRequest(BaseModel):
    do_reset:Optional[int] = 0
    
class SearchRequest(BaseModel):
    text: str = Field(..., min_length=1)
    limit: Optional[int] = Field(5, gt=0)
