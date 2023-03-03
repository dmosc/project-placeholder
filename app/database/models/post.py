from peewee import Model, CharField, DateTimeField
from datetime import datetime

from app.database.models.base_model import BaseModel


class Post(BaseModel):
    name = CharField()
    email = CharField()
    content = CharField()
