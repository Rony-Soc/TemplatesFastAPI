from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_current_active_user
from app.models.user import UserInDB
from app.services.llm_client import llm_client

router = APIRouter()


class TextGenerationRequest(BaseModel):
    prompt: str
    model: Optional[str] = None


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    messages: List[ChatMessage]
    model: Optional[str] = None
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000


class TextResponse(BaseModel):
    text: str


@router.post("/generate", response_model=TextResponse)
async def generate_text(
    request: TextGenerationRequest,
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Generate text using the configured LLM provider"""
    try:
        text = await llm_client.generate_text(request.prompt, request.model)
        return TextResponse(text=text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat", response_model=TextResponse)
async def chat_completion(
    request: ChatCompletionRequest,
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Generate chat completion using the configured LLM provider"""
    try:
        # Convert Pydantic models to dict for the LLM client
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        text = await llm_client.chat_completion(
            messages=messages,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        return TextResponse(text=text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models")
async def get_available_models(
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Get available models for the configured LLM provider"""
    if llm_client.provider == "openai":
        return {
            "provider": "openai",
            "models": ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]
        }
    elif llm_client.provider == "gemini":
        return {
            "provider": "gemini",
            "models": ["gemini-pro", "gemini-pro-vision"]
        }
    else:
        return {
            "provider": llm_client.provider,
            "models": []
        } 