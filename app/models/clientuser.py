from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
   
    clients = relationship("Client", back_populates="user") 

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    description = Column(String)
    usermail = Column(String)
    phoneno = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)  
    user = relationship("User", back_populates="clients")

# from app.database.database import Base
# from sqlalchemy import Column,Integer,String
# # from app.database import Base

# class Client(Base):
#     __tablename__ = "clients"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     location = Column(String)
#     description = Column(String)
#     usermail = Column(String)
#     phoneno = Column(String)

# from sqlalchemy import Column, Integer, String
# from app.database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)

# class Client(Base):
#     __tablename__ = "clients"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, index=True)
#     user_id = Column(Integer, index=True)