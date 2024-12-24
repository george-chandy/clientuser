
from fastapi import FastAPI
from app.api.v1.route_client_user import router
from app.api.v1.auth import auth_router
from app.database import engine, Base
from app.models.clientuser import User, Client  # Import your models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)  
app.include_router(auth_router)  

@app.get("/")
async def root():
    return {"message": "Hello from my FastAPI app!"}

from fastapi import FastAPI









