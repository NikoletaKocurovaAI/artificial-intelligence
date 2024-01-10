from fastapi import FastAPI

from settings import Settings
from sqlalchemy import create_engine, MetaData, Table, select
from databases import Database


app = FastAPI()

settings = Settings()

username = settings.DB_USER
password = settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
name = settings.DB_NAME

#DATABASE_URL = f"postgres:asyncpg://{username}:{password}@{host}:{port}/{name}"
DATABASE_URL = f"postgresql+asyncpg://{username}:password@{host}:{port}/{name}?password={password}"

database = Database(DATABASE_URL)
metadata = MetaData()

robot = Table('your_table', metadata)

@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

@app.get("/read_data")
async def read_data():
    query = select([robot])
    result = await database.fetch_all(query)

    return {"data": result}
