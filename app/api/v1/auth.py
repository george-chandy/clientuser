from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv
import os

from app.database import get_db
from app.schemas import Token
from app.services import clientservice  # Assuming you have clientservice for user-related operations
from sqlalchemy.orm import Session

# Load environment variables from .env file
load_dotenv()

auth_router = APIRouter(
    tags=["auth"],
)

# --- JWT Configuration ---
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not set")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Important: Keep this consistent

# --- Helper Functions ---
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # ... (same as before)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    # ... (same as before)

# --- API Endpoints ---
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # ... (same as before)