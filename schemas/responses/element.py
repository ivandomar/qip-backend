from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from models.element import Element


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