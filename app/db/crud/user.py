from typing import Optional, List
from bson import ObjectId
from app.db.mongodb import get_collection
from app.models.user import UserCreate, UserUpdate, UserInDB, User
from app.core.security import get_password_hash, verify_password


class UserCRUD:
    def __init__(self):
        self.collection = get_collection("users")

    async def create(self, user: UserCreate) -> UserInDB:
        """Create a new user"""
        user_dict = user.dict()
        user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
        
        result = await self.collection.insert_one(user_dict)
        user_dict["_id"] = result.inserted_id
        
        return UserInDB(**user_dict)

    async def get_by_id(self, user_id: str) -> Optional[UserInDB]:
        """Get user by ID"""
        user_dict = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user_dict:
            return UserInDB(**user_dict)
        return None

    async def get_by_email(self, email: str) -> Optional[UserInDB]:
        """Get user by email"""
        user_dict = await self.collection.find_one({"email": email})
        if user_dict:
            return UserInDB(**user_dict)
        return None

    async def get_multi(self, skip: int = 0, limit: int = 100) -> List[UserInDB]:
        """Get multiple users"""
        cursor = self.collection.find().skip(skip).limit(limit)
        users = []
        async for user_dict in cursor:
            users.append(UserInDB(**user_dict))
        return users

    async def update(self, user_id: str, user_update: UserUpdate) -> Optional[UserInDB]:
        """Update user"""
        update_data = user_update.dict(exclude_unset=True)
        
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
        
        update_data["updated_at"] = UserInDB.updated_at.default_factory()
        
        result = await self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        
        if result.modified_count:
            return await self.get_by_id(user_id)
        return None

    async def delete(self, user_id: str) -> bool:
        """Delete user"""
        result = await self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    async def authenticate(self, email: str, password: str) -> Optional[UserInDB]:
        """Authenticate user with email and password"""
        user = await self.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user_crud = UserCRUD() 