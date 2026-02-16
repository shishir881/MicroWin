"""
One-time migration to add gamification columns to the users table.
Run this once: python migrate_gamification.py
"""
import asyncio
from sqlalchemy import text
from app.db.session import engine

MIGRATIONS = [
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS streak_count INTEGER DEFAULT 0;",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS last_completion_date DATE;",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS total_completed INTEGER DEFAULT 0;",
]

async def run_migration():
    async with engine.begin() as conn:
        for sql in MIGRATIONS:
            print(f"Running: {sql}")
            await conn.execute(text(sql))
    print("✅ Migration complete!")

if __name__ == "__main__":
    asyncio.run(run_migration())
