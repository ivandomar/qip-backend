from pydantic import BaseModel
from typing import Optional, List

class NewElementRequestSchema(BaseModel):
    title: str
    content: str
    element_type_id: int
    parent_id: int = None


class ListElementRequestSchema(BaseModel):
    parent_id: int = None


class GetElementRequestSchema(BaseModel):
    id: int


class RemoveElementRequestSchema(BaseModel):
    id: int