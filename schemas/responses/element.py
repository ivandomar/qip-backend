from datetime import datetime
from pydantic import BaseModel
from typing import List


class RemoveElementResponseSchema(BaseModel):
    mesage: str

class ElementResponseSchema(BaseModel):
    id: int
    title: str
    content: str
    element_type_id: int
    created_at: datetime
    updated_at: datetime


class ElementListResponseSchema(BaseModel):
    elements:List[ElementResponseSchema]