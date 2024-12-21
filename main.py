
from fastapi import FastAPI
from app.api.v1.route_client_user import router

app = FastAPI()

app.include_router(router)  

@app.get("/")
async def root():
    return {"message": "Hello from my FastAPI app!"}