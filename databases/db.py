import asyncio
from tortoise import Tortoise, exceptions

async def init_db():
    try:
        await Tortoise.init(
            db_url='sqlite://my_notes.db',
            modules={'models': ['models.user', 'models.note']}
        )
        await Tortoise.generate_schemas()
    except exceptions.ConnectionError as e:
        print(f"Failed to connect to the database: {e}")
        await asyncio.sleep(5)
        await init_db()

