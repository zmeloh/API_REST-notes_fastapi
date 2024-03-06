import asyncio
from tortoise import Tortoise, exceptions
from models.user import User

async def add_initial_data():
    # Créer des utilisateurs de test
    users = [
        {"username": "utilisateur1", "password": "motdepasse1"},
        {"username": "utilisateur2", "password": "motdepasse2"},
        {"username": "utilisateur3", "password": "motdepasse3"},
    ]

    for user_data in users:
        try:
            await User.create(**user_data)
            print(f"User {user_data['username']} added.")
        except exceptions.IntegrityError:
            print(f"User {user_data['username']} already exists.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        await Tortoise.init(
            db_url='sqlite://my_notes.db',
            modules={'models': ['models.user', 'models.note']}
        )
        await add_initial_data()
    finally:
        await Tortoise.close_connections()


import asyncio
from tortoise import Tortoise, exceptions
from models.user import User

async def add_initial_data():
    # Créer des utilisateurs de test
    users = [
        {"username": "utilisateur1", "password": "motdepasse1"},
        {"username": "utilisateur2", "password": "motdepasse2"},
        {"username": "utilisateur
