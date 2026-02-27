# SupplyChain AI - FastAPI Backend

AI-Powered Supplier Risk Management Backend API

## Overview

This is the FastAPI backend for the SupplyChain AI application. It provides RESTful API endpoints for user authentication and management.

## Features

- ✅ REST API endpoints (Login, Register, Logout)
- ✅ Pydantic models for request validation
- ✅ CORS enabled for frontend connection
- ✅ In-memory storage (easily replaceable with database)
- ✅ Health check endpoint
- ✅ Clean, production-style code with comments
- ✅ Modular architecture for easy database integration

## Project Structure

```
backend/
├── __init__.py         # Package initialization
├── main.py             # FastAPI application entry point
├── models.py           # Pydantic models for validation
├── routes.py           # API endpoints
├── auth.py             # Authentication logic
├── database.py         # Database placeholder
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation

1. Navigate to the backend directory:
   
```
bash
   cd backend
   
```

2. Create a virtual environment (optional but recommended):
   
```
bash
   python -m venv venv
   
```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Install dependencies:
   
```
bash
   pip install -r requirements.txt
   
```

## Running the Server

### Development Mode

Run with auto-reload:
```
bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Or run directly from the backend directory:
```
bash
cd backend
python main.py
```

### Production Mode

Run with multiple workers:
```
bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI JSON**: http://localhost:8000/api/openapi.json

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/login` | User login |
| POST | `/api/register` | User registration |
| POST | `/api/logout` | User logout |
| GET | `/api/health` | Health check |
| GET | `/api/users` | Get all users (testing) |
| GET | `/` | Root endpoint |

## Demo Credentials

The following demo users are available for testing:

| Email | Password |
|-------|----------|
| admin@supplychain.ai | any password |
| user@supplychain.ai | any password |

## Example Requests

### Login Request

```
bash
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@supplychain.ai",
    "password": "demo123",
    "remember_me": false
  }'
```

### Health Check

```
bash
curl "http://localhost:8000/api/health"
```

## Frontend Integration

To connect your frontend to this backend:

1. Update your frontend API calls to use:
   
```
   http://localhost:8000/api/login
   
```

2. The login endpoint expects:
   
```
json
   {
     "email": "user@example.com",
     "password": "password123",
     "remember_me": false
   }
   
```

3. The response will include:
   
```
json
   {
     "success": true,
     "message": "Login successful",
     "token": "generated_token",
     "user": {
       "email": "user@example.com",
       "username": "username",
       "full_name": "Full Name",
       "is_verified": true
     }
   }
   
```

## Future Database Integration

The code is structured to easily integrate with a database:

1. **Update `database.py`**: Replace in-memory storage with actual database connection
2. **Update `auth.py`**: Integrate password hashing (bcrypt) and JWT tokens
3. **Update `models.py`**: Add database-specific models if needed
4. **Update `requirements.txt`**: Add database driver dependencies

Supported databases:
- PostgreSQL (asyncpg, SQLAlchemy)
- MongoDB (motor)
- MySQL (aiomysql)
- SQLite (aiosqlite)

## Logging

The application uses Python's built-in logging. Logs are output to the console.

To enable debug logging, modify the log level in `main.py`:
```
python
logging.basicConfig(level=logging.DEBUG, ...)
```

## License

© 2024 SupplyChain AI. All rights reserved.
