from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import init_db
from app.routers import matches

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Tournament Manager API",
    description="Асинхронное API для управления киберспортивными турнирами",
    version="1.0.0"
)

app.include_router(matches.router)