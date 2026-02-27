"""
FastAPI application main entry point.

This is the main application file for the SupplyChain AI backend.
It configures the FastAPI app, middleware, CORS, and registers all routers.

Features:
- RESTful API endpoints
- CORS enabled for frontend connection
- Pydantic models for request validation
- In-memory storage (easily replaceable with database)
- Health check endpoint
- Modular route structure

To run the server:
    uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime
import logging

# Import routes
from backend.routes import router
from backend.database import database

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# FastAPI Application Setup
# ============================================================================

# Create FastAPI application instance
app = FastAPI(
    title="SupplyChain AI API",
    description="AI-Powered Supplier Risk Management API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)


# ============================================================================
# CORS Configuration
# ============================================================================

# Configure CORS to allow frontend connection
# In production, replace ["*"] with specific frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# ============================================================================
# Application Events (Startup/Shutdown)
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """
    Startup event handler.
    
    Called when the application starts up.
    Initializes database connection and logs startup.
    """
    logger.info("=" * 50)
    logger.info("SupplyChain AI API Starting Up")
    logger.info("=" * 50)
    
    # Initialize database connection
    await database.connect()
    logger.info("Database connected (in-memory)")
    
    # Log startup information
    logger.info(f"API Documentation: http://localhost:8000/api/docs")
    logger.info(f"ReDoc Documentation: http://localhost:8000/api/redoc")
    logger.info("=" * 50)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Shutdown event handler.
    
    Called when the application shuts down.
    Cleans up resources and closes connections.
    """
    logger.info("=" * 50)
    logger.info("SupplyChain AI API Shutting Down")
    logger.info("=" * 50)
    
    # Close database connection
    await database.disconnect()
    logger.info("Database disconnected")
    
    logger.info("Shutdown complete")


# ============================================================================
# Global Exception Handler
# ============================================================================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler for unhandled errors.
    
    Args:
        request: The incoming request
        exc: The exception that was raised
        
    Returns:
        JSON error response
    """
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "error": str(exc) if logger.level == logging.DEBUG else "An error occurred"
        }
    )


# ============================================================================
# Root Endpoint
# ============================================================================

@app.get("/")
async def root():
    """
    Root endpoint.
    
    Returns basic information about the API.
    
    Returns:
        JSON response with API information
    """
    return {
        "name": "SupplyChain AI API",
        "version": "1.0.0",
        "description": "AI-Powered Supplier Risk Management API",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat(),
        "endpoints": {
            "docs": "/api/docs",
            "health": "/api/health",
            "login": "/api/login",
            "register": "/api/register",
            "logout": "/api/logout",
            "users": "/api/users"
        }
    }


# ============================================================================
# Register API Routes
# ============================================================================

# Include all API routes
app.include_router(router)


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    """
    Main entry point for running the application directly.
    
    For development, use:
        uvicorn backend.main:app --reload
    
    For production, use:
        uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 4
    """
    import uvicorn
    
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
