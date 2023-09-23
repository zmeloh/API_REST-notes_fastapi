import asyncio
from tortoise import Tortoise
from models.user import User

async def add_initial_data():
    # Créer des utilisateurs de test
    users = [
        {"username": "utilisateur1", "password": "motdepasse1"},
        {"username": "utilisateur2", "password": "motdepasse2"},
        {"username": "utilisateur3", "password": "motdepasse3"},
    ]

    for user_data in users:
        await User.create(**user_data)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Tortoise.init(
        db_url='sqlite://my_notes.db',
        modules={'models': ['models.user', 'models.note']}
    ))
    loop.run_until_complete(add_initial_data())
    loop.run_until_complete(Tortoise.close_connections())
