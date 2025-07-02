from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Global database client
client: AsyncIOMotorClient = None
database = None


async def connect_to_mongo():
    """Create database connection."""
    global client, database
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    database = client[settings.MONGODB_DB_NAME]
    print("Connected to MongoDB.")


async def close_mongo_connection():
    """Close database connection."""
    global client
    if client:
        client.close()
        print("Disconnected from MongoDB.")


def get_database() -> AsyncIOMotorClient:
    """Get database instance."""
    return database


def get_collection(collection_name: str):
    """Get collection instance."""
    return database[collection_name] 