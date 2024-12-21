from pydantic import BaseModel

class ClientUserBase(BaseModel):
    name:str
    location:str
    description:str
    usermail:str
    phoneno:str


class ClientUserNew(ClientUserBase):
    pass

class clientUser(ClientUserBase):
    id:int





