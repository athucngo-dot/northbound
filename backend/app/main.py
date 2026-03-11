from fastapi import FastAPI

from app.api.routes import users, auth

app = FastAPI(title="Northbound API")

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}