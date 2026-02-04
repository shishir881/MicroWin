from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite file path (yo backend folder mah basxa)
DATABASE_URL = "sqlite+aiosqlite:///./atomize.db"

# Engine create garne (Async support ko lagi)
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory (Database sanga kura garna)
SessionLocal = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

Base = declarative_base()

# Dependency: Check out "get_db" function later
async def get_db():
    async with SessionLocal() as session:
        yield session