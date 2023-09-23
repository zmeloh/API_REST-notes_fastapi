from tortoise import fields, models
from pydantic import BaseModel
from typing import List

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)  # Vous devriez utiliser un stockage sécurisé des mots de passe en production

    def __str__(self):
        return self.username
    
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str