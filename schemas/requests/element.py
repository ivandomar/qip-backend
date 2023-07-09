from pydantic import BaseModel
from typing import List

# TODO: cross validate content against element type
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