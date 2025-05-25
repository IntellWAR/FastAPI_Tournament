from fastapi import FastAPI
from routers import match

app = FastAPI(
    title="Турнирная сетка",
    description="API для управления историей матчей киберспортивных турниров"
)

app.include_router(match.router)