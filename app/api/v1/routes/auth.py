from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import Token, UserLogin, UserRegister, UserResponse
from app.services.auth_service import auth_service
from app.models.user import UserInDB

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(user_data: UserRegister):
    """Register a new user"""
    user = await auth_service.register(user_data)
    return UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active,
        is_superuser=user.is_superuser
    )


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login user and return access token"""
    user_data = UserLogin(email=form_data.username, password=form_data.password)
    user = await auth_service.authenticate(user_data)
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    access_token = auth_service.create_token(user)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login-json", response_model=Token)
async def login_json(user_data: UserLogin):
    """Login user with JSON data and return access token"""
    user = await auth_service.authenticate(user_data)
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    access_token = auth_service.create_token(user)
    return {"access_token": access_token, "token_type": "bearer"} 