from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}

    for err in exc.errors():
        field = err["loc"][-1]   # get the field name that caused the error
        message = err["msg"]     # default error message from FastAPI/Pydantic

        # customize messages
        if field == "email":
            message = "Email address is not valid."

        errors[field] = message

    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "errors": errors
        }
    )

def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail if isinstance(exc.detail, str) else "Error",
            "errors": {}
        }
    )