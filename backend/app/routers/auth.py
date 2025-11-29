from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.database import get_db
from backend.app.schemas.user import UserLogin, Token
from backend.app.core.config import settings
import structlog

log = structlog.get_logger()

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=Token)
async def login(
    credentials: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Login endpoint - validates credentials and returns JWT token
    
    TODO: Implement actual authentication logic
    """
    log.info("login_attempt", email=credentials.email)
    
    # Placeholder - replace with actual auth logic
    if credentials.email == "test@example.com" and credentials.password == "password":
        return Token(
            access_token="dummy_jwt_token_replace_with_real_implementation",
            token_type="bearer"
        )
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )


@router.post("/register", response_model=Token)
async def register(
    credentials: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Registration endpoint - creates new user and returns JWT token
    
    TODO: Implement user creation logic
    """
    log.info("register_attempt", email=credentials.email)
    
    # Placeholder
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Registration not yet implemented"
    )
