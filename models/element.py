from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Element(Base):
    __tablename__ = 'element'

    id = Column("id", Integer, primary_key=True)
    title = Column(String(63), nullable=False)
    content = Column(String(255))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime)
    
    element_type_id = Column(Integer, ForeignKey("element_type.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey('element.id'))

    children = relationship("Element")

    def __init__(self, title:str, content:str, element_type_id:int, parent_id:int):
        self.title = title
        self.content = content
        self.element_type_id = element_type_id
        self.parent_id = parent_id
