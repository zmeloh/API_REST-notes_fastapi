from typing import List
from tortoise.queryset import QuerySet
from models.note import Note
from models.user import User

async def create_note(user: User, title: str, content: str):
    note = await Note.create(user=user, title=title, content=content)
    return note

async def get_note_by_id(note_id: int) -> Note:
    note = await Note.get(id=note_id)
    return note

async def get_notes_by_user(user: User):
    async def get_notes_by_user(user) -> List[Note]:
        notes: QuerySet[Note] = Note.filter(user=user).order_by('-created_at')
        return await notes.all()
    
async def update_note(note: Note, title: str, content: str):
    note.title = title
    note.content = content
    await note.save()
    return note

async def delete_note(note: Note):
    await note.delete()
