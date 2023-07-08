from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

db_path = "database/data"

if not os.path.exists(db_path):
   os.makedirs(db_path)

db_url = f'sqlite:///{db_path}/qip.sqlite3'

engine = create_engine(db_url, echo=False)

session = sessionmaker(engine)

if not database_exists(engine.url):
    create_database(engine.url) 