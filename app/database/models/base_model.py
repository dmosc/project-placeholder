import os

from peewee import Model, DateTimeField
from datetime import datetime

from app.lib.secrets_manager import SecretsManager
from app.database.lib import Database


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = Database.get_instance()
