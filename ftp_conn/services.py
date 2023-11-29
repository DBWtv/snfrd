from cryptography.fernet import Fernet
from django.conf import settings


class Encoder(Fernet):

    def __init__(self, key: str):
        super().__init__(key)

    def encrypt(self, password: str) -> str:
        return super().encrypt(password.encode()).decode()

    def decrypt(self, password: str) -> str:
        return super().decrypt(password.encode()).decode()


ENCODER = Encoder(settings.FTP_PASS_HASH_KEY)
