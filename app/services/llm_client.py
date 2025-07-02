import httpx
from typing import Optional, Dict, Any
from app.core.config import settings


class LLMClient:
    def __init__(self):
        self.provider = settings.LLM_PROVIDER
        self.openai_api_key = settings.OPENAI_API_KEY
        self.gemini_api_key = settings.GEMINI_API_KEY

    async def generate_text(self, prompt: str, model: Optional[str] = None) -> str:
        """Generate text using the configured LLM provider"""
        if self.provider == "openai":
            return await self._openai_generate(prompt, model)
        elif self.provider == "gemini":
            return await self._gemini_generate(prompt, model)
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")

    async def _openai_generate(self, prompt: str, model: Optional[str] = None) -> str:
        """Generate text using OpenAI API"""
        if not self.openai_api_key:
            raise ValueError("OpenAI API key not configured")
        
        model = model or "gpt-3.5-turbo"
        url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000,
            "temperature": 0.7
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]

    async def _gemini_generate(self, prompt: str, model: Optional[str] = None) -> str:
        """Generate text using Gemini API"""
        if not self.gemini_api_key:
            raise ValueError("Gemini API key not configured")
        
        model = model or "gemini-pro"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        
        params = {"key": self.gemini_api_key}
        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params, json=data)
            response.raise_for_status()
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]

    async def chat_completion(
        self, 
        messages: list, 
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """Generate chat completion"""
        if self.provider == "openai":
            return await self._openai_chat(messages, model, temperature, max_tokens)
        elif self.provider == "gemini":
            return await self._gemini_chat(messages, model, temperature, max_tokens)
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")

    async def _openai_chat(
        self, 
        messages: list, 
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """OpenAI chat completion"""
        if not self.openai_api_key:
            raise ValueError("OpenAI API key not configured")
        
        model = model or "gpt-3.5-turbo"
        url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]

    async def _gemini_chat(
        self, 
        messages: list, 
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """Gemini chat completion"""
        if not self.gemini_api_key:
            raise ValueError("Gemini API key not configured")
        
        model = model or "gemini-pro"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        
        params = {"key": self.gemini_api_key}
        
        # Convert messages to Gemini format
        contents = []
        for msg in messages:
            contents.append({
                "parts": [{"text": msg["content"]}],
                "role": msg["role"]
            })
        
        data = {
            "contents": contents,
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens
            }
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params, json=data)
            response.raise_for_status()
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]


llm_client = LLMClient() 