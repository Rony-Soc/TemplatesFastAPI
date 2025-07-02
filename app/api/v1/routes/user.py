from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import UserResponse
from app.models.user import UserInDB, UserUpdate
from app.api.deps import get_current_active_user, get_current_superuser
from app.db.crud.user import user_crud

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    """Get current user information"""
    return UserResponse(
        id=str(current_user.id),
        email=current_user.email,
        full_name=current_user.full_name,
        is_active=current_user.is_active,
        is_superuser=current_user.is_superuser
    )


@router.put("/me", response_model=UserResponse)
async def update_user_me(
    user_update: UserUpdate,
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Update current user information"""
    updated_user = await user_crud.update(str(current_user.id), user_update)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(
        id=str(updated_user.id),
        email=updated_user.email,
        full_name=updated_user.full_name,
        is_active=updated_user.is_active,
        is_superuser=updated_user.is_superuser
    )


@router.get("/", response_model=List[UserResponse])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_superuser)
):
    """Get all users (superuser only)"""
    users = await user_crud.get_multi(skip=skip, limit=limit)
    return [
        UserResponse(
            id=str(user.id),
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
            is_superuser=user.is_superuser
        )
        for user in users
    ]


@router.get("/{user_id}", response_model=UserResponse)
async def read_user(
    user_id: str,
    current_user: UserInDB = Depends(get_current_superuser)
):
    """Get user by ID (superuser only)"""
    user = await user_crud.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active,
        is_superuser=user.is_superuser
    )


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str,
    user_update: UserUpdate,
    current_user: UserInDB = Depends(get_current_superuser)
):
    """Update user (superuser only)"""
    updated_user = await user_crud.update(user_id, user_update)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(
        id=str(updated_user.id),
        email=updated_user.email,
        full_name=updated_user.full_name,
        is_active=updated_user.is_active,
        is_superuser=updated_user.is_superuser
    )


@router.delete("/{user_id}")
async def delete_user(
    user_id: str,
    current_user: UserInDB = Depends(get_current_superuser)
):
    """Delete user (superuser only)"""
    success = await user_crud.delete(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {"message": "User deleted successfully"} 