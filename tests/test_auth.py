import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient, test_user):
    """Test user registration."""
    response = await client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 200
    
    data = response.json()
    assert data["email"] == test_user["email"]
    assert data["full_name"] == test_user["full_name"]
    assert "password" not in data


@pytest.mark.asyncio
async def test_register_duplicate_user(client: AsyncClient, test_user):
    """Test registration with duplicate email."""
    # Register first user
    response = await client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 200
    
    # Try to register with same email
    response = await client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]


@pytest.mark.asyncio
async def test_login_user(client: AsyncClient, test_user):
    """Test user login."""
    # Register user first
    response = await client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 200
    
    # Login
    login_data = {
        "username": test_user["email"],
        "password": test_user["password"]
    }
    response = await client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient, test_user):
    """Test login with invalid credentials."""
    # Register user first
    response = await client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 200
    
    # Try to login with wrong password
    login_data = {
        "username": test_user["email"],
        "password": "wrongpassword"
    }
    response = await client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 401 