# 🚀 FastAPI Template

[![Use this template](https://img.shields.io/badge/Use%20this%20template-brightgreen?style=for-the-badge&logo=github)](https://github.com/krishnakamalbaishnab/TemplatesFastAPI)

A production-ready FastAPI template with MongoDB integration, JWT authentication, and LLM support. Perfect for building scalable APIs with modern Python practices.

## ✨ Features

- **FastAPI Backend** - Modern, fast web framework for building APIs
- **MongoDB Integration** - Async database operations with Motor
- **JWT Authentication** - Secure user authentication and authorization
- **LLM Integration** - Support for OpenAI and Gemini APIs
- **Docker Support** - Containerized development and deployment
- **Comprehensive Testing** - Pytest setup with async support
- **Production Ready** - Security, CORS, environment configuration
- **API Documentation** - Automatic Swagger/OpenAPI docs at `/docs`

## 🏗️ Project Structure

```
├── app/
│   ├── api/
│   │   ├── deps.py              # Dependencies and authentication
│   │   └── v1/
│   │       ├── api.py           # Main API router
│   │       └── routes/
│   │           ├── auth.py      # Authentication endpoints
│   │           ├── user.py      # User management endpoints
│   │           └── llm.py       # LLM integration endpoints
│   ├── core/
│   │   ├── config.py            # Settings and configuration
│   │   └── security.py          # JWT and password utilities
│   ├── db/
│   │   ├── mongodb.py           # Database connection
│   │   └── crud/
│   │       └── user.py          # User CRUD operations
│   ├── models/
│   │   └── user.py              # Pydantic models
│   ├── schemas/
│   │   └── auth.py              # Request/response schemas
│   └── services/
│       ├── auth_service.py      # Authentication business logic
│       └── llm_client.py        # LLM integration service
├── tests/
│   ├── conftest.py              # Pytest configuration
│   ├── test_auth.py             # Authentication tests
│   └── test_users.py            # User endpoint tests
├── main.py                      # FastAPI application entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Production Docker image
├── docker-compose.yml           # Local development setup
├── env.example                  # Environment variables template
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- MongoDB (local or cloud)
- Docker & Docker Compose (optional)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/krishnakamalbaishnab/TemplatesFastAPI.git
   cd TemplatesFastAPI
   ```

2. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start MongoDB** (if using local MongoDB)
   ```bash
   # Using Docker
   docker run -d -p 27017:27017 --name mongodb mongo:7.0
   
   # Or install MongoDB locally
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

### Using Docker Compose

1. **Start all services**
   ```bash
   docker-compose up -d
   ```

2. **Access services**
   - FastAPI: http://localhost:8000
   - MongoDB Express: http://localhost:8081 (admin/admin123)

3. **View logs**
   ```bash
   docker-compose logs -f app
   ```

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```env
# Security
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# MongoDB
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=fastapi_template

# LLM Settings
OPENAI_API_KEY=your-openai-api-key
GEMINI_API_KEY=your-gemini-api-key
LLM_PROVIDER=openai  # or "gemini"

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
```

## 📚 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login with form data
- `POST /api/v1/auth/login-json` - Login with JSON

### Users
- `GET /api/v1/users/me` - Get current user (authenticated)
- `PUT /api/v1/users/me` - Update current user (authenticated)
- `GET /api/v1/users/` - Get all users (superuser only)
- `GET /api/v1/users/{user_id}` - Get user by ID (superuser only)
- `PUT /api/v1/users/{user_id}` - Update user (superuser only)
- `DELETE /api/v1/users/{user_id}` - Delete user (superuser only)

### LLM Integration
- `POST /api/v1/llm/generate` - Generate text (authenticated)
- `POST /api/v1/llm/chat` - Chat completion (authenticated)
- `GET /api/v1/llm/models` - Get available models (authenticated)

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v
```

## 🐳 Docker Deployment

### Build and run with Docker

```bash
# Build the image
docker build -t fastapi-template .

# Run the container
docker run -p 8000:8000 --env-file .env fastapi-template
```

### Production deployment

1. **Build production image**
   ```bash
   docker build -t fastapi-template:prod .
   ```

2. **Run with production settings**
   ```bash
   docker run -d \
     --name fastapi-app \
     -p 8000:8000 \
     --env-file .env.prod \
     fastapi-template:prod
   ```

## 🔒 Security Features

- **JWT Authentication** - Secure token-based authentication
- **Password Hashing** - BCrypt password hashing
- **CORS Protection** - Configurable CORS settings
- **Input Validation** - Pydantic model validation
- **Environment Configuration** - Secure configuration management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Motor](https://motor.readthedocs.io/) - Async MongoDB driver
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [Python-Jose](https://python-jose.readthedocs.io/) - JWT implementation

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

**Made with ❤️ for the FastAPI community** 