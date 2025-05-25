from app.config import settings as cnf
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# Только асинхронное подключение
ASYNC_DB_URL = f"postgresql+asyncpg://{cnf.db_username}:{cnf.db_password}@{cnf.db_host}:{cnf.db_port}/{cnf.db_name}"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)

# Создаем асинхронную сессию
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_async_session() -> AsyncSession:
    """
    Генератор асинхронных сессий для Dependency Injection.
    Использование:
    
    @router.post("/matches")
    async def create_match(
        match: MatchCreate,
        session: AsyncSession = Depends(get_async_session)
    ):
        ...
    """
    async with async_session() as session:
        yield session

async def init_db():
    """
    Создает таблицы при старте приложения.
    Вызывается из lifespan в main.py.
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)