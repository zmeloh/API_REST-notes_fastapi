from tortoise import fields, models
from pydantic import BaseModel
from typing import List
import datetime
from .user import UserOut
class Note(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField('models.User', related_name='notes')

    def __str__(self):
        return self.title

class NoteIn(BaseModel):
    title: str
    content: str

class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime
    user: UserOut