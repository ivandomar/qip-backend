from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

from .seeders.element_type import element_type_seeder
from models import Base, Element, ElementType

db_path = "database/data"

if not os.path.exists(db_path):
   os.makedirs(db_path)

db_url = f'sqlite:///{db_path}/qip.sqlite3'

engine = create_engine(db_url, echo=True)

Session = sessionmaker(engine)

if not database_exists(engine.url):
    create_database(engine.url) 

    Base.metadata.create_all(engine)

    seeding_session = Session()
    seeding_session.add_all(element_type_seeder)
    seeding_session.commit()