from models.user import User

async def create_user(username: str, password: str):
    user = await User.create(username=username, password=password)
    return user

async def get_user_by_id(user_id: int):
    user = await User.get(id=user_id)
    return user

async def get_user_by_username(username: str):
    user = await User.get(username=username)
    return user

async def get_all_users():
    users = await User.all()
    return users
