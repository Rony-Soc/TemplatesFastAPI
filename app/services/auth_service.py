from typing import Optional
from fastapi import HTTPException, status
from app.db.crud.user import user_crud
from app.models.user import UserCreate, UserInDB
from app.schemas.auth import UserLogin, UserRegister
from app.core.security import create_access_token


class AuthService:
    @staticmethod
    async def register(user_data: UserRegister) -> UserInDB:
        """Register a new user"""
        # Check if user already exists
        existing_user = await user_crud.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create new user
        user_create = UserCreate(
            email=user_data.email,
            password=user_data.password,
            full_name=user_data.full_name
        )
        
        return await user_crud.create(user_create)

    @staticmethod
    async def authenticate(user_data: UserLogin) -> Optional[UserInDB]:
        """Authenticate user with email and password"""
        user = await user_crud.authenticate(user_data.email, user_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user

    @staticmethod
    def create_token(user: UserInDB) -> str:
        """Create access token for user"""
        token_data = {"sub": str(user.id), "email": user.email}
        return create_access_token(data=token_data)


auth_service = AuthService() 