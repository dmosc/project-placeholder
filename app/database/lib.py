from app.lib.secrets_manager import SecretsManager
from peewee import MySQLDatabase


class Database(object):
    _instance = None

    def __init__(self):
        raise RuntimeError("call get_instance() instead.")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = MySQLDatabase(
                database=SecretsManager.get_env("MYSQL_DATABASE"),
                user=SecretsManager.get_env("MYSQL_USER"),
                password=SecretsManager.get_env("MYSQL_PASSWORD"),
                host=SecretsManager.get_env("MYSQL_HOST"),
                port=3306
            )
            cls._instance.connect()

        return cls._instance
