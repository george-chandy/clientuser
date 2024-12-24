from pydantic import BaseModel, EmailStr

# class ClientUserBase(BaseModel):
#     name:str
#     location:str
#     description:str
#     usermail:str
#     phoneno:str


# class ClientUserNew(ClientUserBase):
#     pass

# class clientUser(ClientUserBase):
#     id:int


from pydantic import BaseModel, EmailStr

class ClientUserBase(BaseModel):
    name: str
    location: str
    description: str | None = None  # Optional field
    usermail: EmailStr
    phoneno: str

class ClientUserNew(ClientUserBase):
    pass  # Inherit all fields from ClientUserBase

class ClientUser(ClientUserBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str

