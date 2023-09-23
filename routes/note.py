from fastapi import APIRouter, HTTPException, Path
from tortoise.contrib.fastapi import HTTPNotFoundError
from services.note_service import create_note, get_note_by_id, get_notes_by_user, update_note, delete_note
from services.user_service import get_user_by_id
from models.note import NoteIn, NoteOut
from typing import List

router = APIRouter()

@router.post("/users/{user_id}/notes/", response_model=NoteOut, responses={404: {"model": HTTPNotFoundError}})
async def create_new_note(user_id: int, note_in: NoteIn):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    note = await create_note(user, note_in.title, note_in.content)
    return note

@router.get("/users/{user_id}/notes/{note_id}/", response_model=NoteOut, responses={404: {"model": HTTPNotFoundError}})
async def get_note(user_id: int, note_id: int):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    note = await get_note_by_id(note_id)
    if note is None or note.user.id != user.id:
        raise HTTPException(status_code=404, detail="Note non trouvée")
    return note

@router.get("/users/{user_id}/notes/", response_model=List[NoteOut], responses={404: {"model": HTTPNotFoundError}})
async def get_user_notes(user_id: int):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    notes = await get_notes_by_user(user)
    return notes

@router.put("/users/{user_id}/notes/{note_id}/", response_model=NoteOut, responses={404: {"model": HTTPNotFoundError}})
async def update_user_note(user_id: int, note_id: int, note_in: NoteIn):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    note = await get_note_by_id(note_id)
    if note is None or note.user.id != user.id:
        raise HTTPException(status_code=404, detail="Note non trouvée")
    
    updated_note = await update_note(note, note_in.title, note_in.content)
    return updated_note

@router.delete("/users/{user_id}/notes/{note_id}/", response_model=NoteOut, responses={404: {"model": HTTPNotFoundError}})
async def delete_user_note(user_id: int, note_id: int):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    note = await get_note_by_id(note_id)
    if note is None or note.user.id != user.id:
        raise HTTPException(status_code=404, detail="Note non trouvée")
    
    deleted_note = await delete_note(note)
    return deleted_note
