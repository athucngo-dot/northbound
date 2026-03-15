# Northbound

Project Status: **Work in Progress**

Northbound is a full-stack project management application.

It allows users to manage organizations, projects, issues, and activities.

## Tech Stack

Backend:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Redis

Frontend:
- React
- Vite

## Project Structure

northbound/
- backend/ -> FastAPI backend
- frontend/ -> React frontend

## Run Backend

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

## Run Frontend

cd frontend
npm install
npm run dev