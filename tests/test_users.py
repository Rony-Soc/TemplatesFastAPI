import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient, auth_headers):
    """Test getting current user information."""
    response = await client.get("/api/v1/users/me", headers=auth_headers)
    assert response.status_code == 200
    
    data = response.json()
    assert "email" in data
    assert "full_name" in data
    assert "id" in data


@pytest.mark.asyncio
async def test_get_current_user_unauthorized(client: AsyncClient):
    """Test getting current user without authentication."""
    response = await client.get("/api/v1/users/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_update_current_user(client: AsyncClient, auth_headers):
    """Test updating current user information."""
    update_data = {
        "full_name": "Updated Name"
    }
    response = await client.put("/api/v1/users/me", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    
    data = response.json()
    assert data["full_name"] == "Updated Name"


@pytest.mark.asyncio
async def test_get_users_unauthorized(client: AsyncClient):
    """Test getting all users without superuser privileges."""
    response = await client.get("/api/v1/users/")
    assert response.status_code == 401 