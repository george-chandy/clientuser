
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.clientuser import Client
# from app.models import clientuser
from app.schemas import schemas
        

def create_client(db:Session, client: schemas.ClientUserNew):

    new_client = Client(     
        name=client.name,  
        location = client.location,
        description = client.description,
        usermail = client.usermail,
        phoneno = client.phoneno     
    )
    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def get_all_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Client).offset(skip).limit(limit).all()

def get_client(db:Session,client_id:int):
    return db.query(Client).filter(Client.id == client_id).first() 

# def update_client(db:Session,client_id:int,client:schemas.ClientUserNew):
#     db_client= db.query(Client).filter(Client.id == client_id).first()
#     for key, value in client.dict().items():
#         setattr(db_client, key, value)
#     db.commit()
#     return db_client

def update_client(db: Session, client_id: int, client: schemas.ClientUserNew):
    db_client = db.query(Client).filter(Client.id == client_id).first()

    if client.name:
        db_client.name = client.name
    if client.location:
        db_client.location = client.location
    if client.description:
        db_client.description = client.description
    if client.usermail:
        db_client.usermail = client.usermail
    if client.phoneno:
        db_client.phoneno = client.phoneno

    db.commit()
    db.refresh(db_client)
    return db_client


def delete_client(db:Session,client_id=int):
    db_client= db.query (Client).filter(Client.id==client_id).first()      
    db.delete(db_client)
    db.commit()
    return db_client

    