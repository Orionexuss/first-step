from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import time
import psycopg2
from  psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}' 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal= sessionmaker(autocommit = False, autoflush= False, bind = engine)

Base = declarative_base() 

#dependency
def get_db():
    db = SessionLocal() # creates a new session
    try:
     yield db # returns a session to use it in the route
    finally:
        db.close() # closes session after it finish using it
        
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi',  user = 'postgres', password = '123fastapi', cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was made successfully")
#         break
#     except Exception as error: 
#         print("Connecting to database failed")
#         print("Error:", error)
#         time.sleep(2)
    