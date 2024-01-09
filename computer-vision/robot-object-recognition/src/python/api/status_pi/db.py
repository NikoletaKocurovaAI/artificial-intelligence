from settings import Settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel


settings = Settings()

username = settings.DB_USER
password = settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
name = settings.DB_NAME

#SQL_ALCHEMY_DB_URL = f"postgres:asyncpg://{username}:{password}@{host}:{port}/{name}"
SQL_ALCHEMY_DB_URL = f"postgresql+asyncpg://{username}:password@{host}:{port}/{name}?password={password}"

engine = create_async_engine(SQL_ALCHEMY_DB_URL, echo=True)


async def init_db():
    from models import Robot

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async_session = sessionmaker(class_=AsyncSession, expire_on_commit=False, autocomit=False)
