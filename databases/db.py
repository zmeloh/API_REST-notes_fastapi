from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='sqlite://my_notes.db',
        modules={'models': ['models.user', 'models.note']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
