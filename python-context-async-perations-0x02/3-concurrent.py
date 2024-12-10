import asyncio
import aiosqlite

async def async_fetch_users(db_name):
    """Fetch all users asynchronously."""
    async with aiosqlite.connect(db_name) as conn:
        async with conn.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users(db_name):
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect(db_name) as conn:
        async with conn.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently(db_name):
    """Fetch both queries concurrently."""
    results = await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name)
    )
    print("All users:", results[0])
    print("Users older than 40:", results[1])

if __name__ == "__main__":
    asyncio.run(fetch_concurrently("users.db"))