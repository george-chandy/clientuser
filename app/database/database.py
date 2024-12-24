# from sqlalchemy import create_engine 
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL="postgresql://sanjana:5454@host:5431/sanjana"

# engine =create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()


from sqlalchemy import Table, create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL/
# SQLALCHEMY_DATABASE_URL = "postgresql://sanjana:5454@localhost:5431/sanjana"
load_dotenv()

DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()

from dotenv import load_dotenv
import os

# Load environment variables from .env file



def create_table_dynamically(table_name, columns):

    try:
        if not engine.dialect.has_table(engine, table_name):
            table = Table(table_name, metadata, *columns)
            metadata.create_all(engine)
            print(f"Table '{table_name}' created successfully.")
        else:
            print(f"Table '{table_name}' already exists.")
    except Exception as e:
        print(f"Error creating table: {e}")


def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base







# if __name__ == "__main__":
#     # Example usage:
#     columns = [
#         Column("id", Integer, primary_key=True, index=True),
#         Column("name", String, index=True),
#         Column("value", String),
#     ]

#     create_table_dynamically("my_dynamic_table", columns)