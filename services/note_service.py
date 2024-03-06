from typing import List, AsyncContextManager
from tortoise.query_set import QuerySet
from tortoise.exceptions import DoesNotExist
from models.note import Note
from models.user import User

async def create_note(user: User, title: str, content: str):
    try:
        note = await Note.create(user=user, title=title, content=content)
        return note
    except Exception as e:
        print(f"Error creating note: {e}")
        return None

async def get_note_by_id(note_id: int) -> Note:
    try:
        note = await Note.get(id=note_id)
        return note
    except DoesNotExist:
        print(f"Note with id {note_id} not found")
        return None

async def get_notes_by_user(user: User) -> List[Note]:
    async def get_notes_by_user(user) -> List[Note]:
        notes: AsyncContextManager[QuerySet[Note]] = Note.filter(user=user).order_by('-created_at')
        return await notes.all()

async def update_note(note: Note, title: str, content: str):
    try:
        note.title = title
        note.content = content
        await note.save()
        return note
    except Exception as e:
        print(f"Error updating note: {e}")
        return None

async def delete_note(note: Note):
    try:
        await note.delete()
        return True
    except Exception as e:
        print(f"Error deleting note: {e}")
        return False
