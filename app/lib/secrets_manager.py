import os

from dotenv import load_dotenv


load_dotenv()


class SecretsManager:
    @staticmethod
    def get_env(name: str) -> str:
        return os.getenv(name)
