from unittest import skip
from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List
from app.database import database
from app.models.clientuser import Client
from app.schemas import schemas
from app.services import clientservice
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)


@router.post("/", response_model=schemas.clientUser)
async def create_client(client: schemas.ClientUserNew, db:Session = Depends(database.get_db)):
    new_client = clientservice.create_client(db=db, client=client)
    return new_client

@router.get("/",response_model=List[schemas.clientUser])
async def read_all_clients(skip:int=0,limit:int=10,db:Session=Depends(database.get_db)):
    read_clients=clientservice.get_all_clients(db=db, skip=skip, limit=limit)
    return read_clients


@router.get("/{client_id}",response_model=schemas.clientUser)
async def read_client(client_id:int,db:Session=Depends(database.get_db)):
    return clientservice.get_client(db=db,client_id=client_id)
   

@router.put("/{client_id}",response_model=schemas.clientUser)
async def update_client(client_id:int,client: schemas.ClientUserNew,db:Session=Depends(database.get_db)):
    updated_client=clientservice.update_client(db=db,client_id=client_id,client=client)
    return updated_client 

@router.delete("/{client_id}")       
async def delete_client(client_id=int,db:Session=Depends(database.get_db)):
    deleted_client=clientservice.delete_client(db=db,client_id=client_id)
    return deleted_client


                        













# client_data = {
#     1: Client(name="Healthgraph", location="New York", description="A valuable client", usermail="john.doe@example.com", phone="123-456-7890"),
#     2: Client(name="santa", location="Los Angeles", description="A new client", usermail="alice.smith@example.com", phone="987-654-3210"),
#     3: Client(name="walmart", location="Chicago", usermail="bob.johnson@example.com", phone="555-123-4567")
# }
# client_id_counter = 4

# @router.get("/")
# async def get_clients():
#     return client_data

# @router.get("/{client_id}")
# async def get_client_details(client_id: int):
#     if client_id in client_data:
#         return client_data[client_id]
#     else:
#         return {"message": "Client not found"}
    

# @router.post("/")
# async def add_client(client : Client):
#     global client_id_counter
#     client_id = client_id_counter
#     client_data[client_id] = client
#     client_id_counter += 1
#     return client


# @router.delete("/{client_id}")
# async def delete_client(client_id: int, client: Client):  
#         client_data.pop(client_id) 


# @router.put("/{client_id}")
# async def update_client(client_id: int, client: Client):  
#     if client_id in client_data:
#         client_data[client_id] = client 
#     return client_data[client_id] 







