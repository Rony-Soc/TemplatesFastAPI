from fastapi import APIRouter
from app.api.v1.routes import auth, user, llm

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(llm.router, prefix="/llm", tags=["llm"]) 