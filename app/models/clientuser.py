
from app.database.database import Base
from sqlalchemy import Column,Integer,String
# from app.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    description = Column(String)
    usermail = Column(String)
    phoneno = Column(String)
