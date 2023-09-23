from fastapi import APIRouter, HTTPException, Path
from tortoise.contrib.fastapi import HTTPNotFoundError
from services.user_service import create_user, get_user_by_id, get_all_users
from models.user import UserIn, UserOut
from typing import List

router = APIRouter()

@router.post("/users/", response_model=UserOut)
async def create_new_user(user_in: UserIn):
    user = await create_user(user_in.username, user_in.password)
    return user

@router.get("/users/{user_id}/", response_model=UserOut, responses={404: {"model": HTTPNotFoundError}})
async def get_user(user_id: int = Path(..., description="L'ID de l'utilisateur à récupérer")):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

@router.get("/users/", response_model=List[UserOut])
async def get_users():
    users = await get_all_users()
    return users
