from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import logger
from app.api.v1.routes import api_router as v1_router
from app.core.config import settings
from app.core.exceptions import http_exception_handler, validation_exception_handler


app = FastAPI(title="Northbound API")


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

# Health check endpoint
@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# Global exception handler for unhandled SQLAlchemy errors
@app.exception_handler(SQLAlchemyError)
async def db_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error("Unhandled DB error", exc_info=True)

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

# Include API routes with versioning prefix v1
app.include_router(v1_router, prefix="/api/v1")

