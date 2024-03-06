from datetime import datetime
from typing import List
from tortoise.models import Model, fields, ForeignKeyField
from tortoise.fields import DatetimeField
from pydantic import BaseModel, Field
from app.schemas.user import UserOut

class Note(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = DatetimeField(auto_now_add=True)
    user = ForeignKeyField('models.User', related_name='notes')

    def __str__(self):
        return self.title

class NoteIn(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(..., min_length=1)

class NoteOut(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    content: str = Field(...)
    created_at: datetime = Field(...)
    user: UserOut = Field(...)
