from pydantic import BaseModel


class NewElementRequestSchema(BaseModel):
    title: str
    content: str = None
    element_type_id: int
    parent_id: int = None


class EditElementIdRequestSchema(BaseModel):
    id: int

class EditElementRequestSchema(BaseModel):
    title: str
    content: str = None


class ListElementRequestSchema(BaseModel):
    parent_id: int = None


class GetElementRequestSchema(BaseModel):
    id: int


class RemoveElementRequestSchema(BaseModel):
    id: int