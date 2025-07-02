import pytest
import asyncio
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from app.main import app
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.core.config import settings


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_db():
    """Create test database connection."""
    # Use test database
    settings.MONGODB_DB_NAME = "test_fastapi_template"
    await connect_to_mongo()
    yield
    await close_mongo_connection()


@pytest.fixture
async def client(test_db):
    """Create test client."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def test_user():
    """Create test user data."""
    return {
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }


@pytest.fixture
async def auth_headers(client, test_user):
    """Get authentication headers for test user."""
    # Register user
    response = await client.post("/api/v1/auth/register", json=test_user)
    assert response.status_code == 200
    
    # Login to get token
    login_data = {
        "username": test_user["email"],
        "password": test_user["password"]
    }
    response = await client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 200
    
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"} 