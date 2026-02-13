import asyncio
from app.db.session import engine, Base
# Import all models to ensure they are registered with Base.metadata
from app.models.task import Task, MicroWinModel
from app.models.user import User 

async def init_db():
    async with engine.begin() as conn:
        print("Dropping existing tables...")
        # WARNING: This deletes existing data. Necessary for schema updates.
        await conn.run_sync(Base.metadata.drop_all)
        
        print("Creating new tables with updated schema...")
        await conn.run_sync(Base.metadata.create_all)
        
    print("Database synchronization complete.")

if __name__ == "__main__":
    asyncio.run(init_db())