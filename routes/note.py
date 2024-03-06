from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from services.note_service import create_note, get_note_by_id, get_notes_by_user, update_note, delete_note
from services.user_service import get_user_by_id
from models.note import NoteIn, NoteOut
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

current_user = OAuth2PasswordBearer()

async def get_current_user(token: str = Depends(current_user)) -> Optional[User]:
    user = await get_user_by_id(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@router.post("/users/{user_id}/notes/", response_model=NoteOut)
async def create_new_note(user_id: int, note_in: NoteIn, user: User = Depends(get_current_user)):
    if user.id != user_id:
        raise HTTPException(status_code=404, detail="User not found")

    note = await create_note(user, note_in.title, note_in.content)
    return note

@router.get("/users/{user_id}/notes/{note_id}/", response_model=NoteOut)
async def get_note(user_id: int, note_id: int, user: User = Depends(get_current_user)):
    if user.id != user_id:
        raise HTTPException(status_code=404, detail="User not found")

    note = await get_note_by_id(note_id)
    if note is None or note.user.id != user.id:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/users/{user_id}/notes/", response_model=List[NoteOut])
async def get_user_notes(user_id: int, user: User = Depends(get_current_user)):
    if user.id != user_id:
        raise HTTPException(status_code=404, detail="User not found")

    notes = await get_notes_by_user(user)
    return notes

@router.put("/users/{user_id}/notes/{note_id}/", response_model=NoteOut)
async def update_user_note(user_id: int, note_id: int, note_in: NoteIn, user: User = Depends(get_current_user)):
    if user.id != user_id:
        raise HTTPException(status_code=404, detail="User not found")

    note = await get_note_by_id(note_id)
    if note is None or note.user.id != user.id:
        raise HTTPException(status_code=404, detail="Note not found")

    updated_note = await update_note(note, note_in.title, note_in.content)
    return updated_note

@router.delete("/users/{user_id}/notes/{note_id}/", response_model=NoteOut)
async def delete_user_note(user_id: int, note_id: int, user: User = Depends(get_current_user)):
    if user.id != user_id:
        raise HTTPException(status_code=404, detail="User not found")

    note = await get_note_by_id(note_id)
    if note is None or note.user.id != user.id:
        raise HTTPException(status_code=404, detail="Note not found")

    deleted_note = await delete_note(note)
    return deleted_note
