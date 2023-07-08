from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from .base import Base


class ElementType(Base):
    __tablename__ = 'element_type'

    id = Column("id", Integer, primary_key=True)
    description = Column(String(16), unique=True)

    def __init__(self, description:str):
        self.description = description
