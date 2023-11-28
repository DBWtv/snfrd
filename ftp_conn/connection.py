from ftplib import FTP
from cryptography.fernet import Fernet


class Encoder(Fernet):

    def __init__(self, key: str):
        super().__init__(key)

    def encrypt(self, password: str) -> str:
        return super().encrypt(password.encode()).decode()

    def decrypt(self, password: str) -> str:
        return super().decrypt(password.encode()).decode()


class FTPConnection(FTP):
    encoder = Encoder

    def __init__(
        self,
        host: str,
        token: str,
        user: str,
        password: str,
        port: int = 21,
    ):
        super().__init__()
        self.encoder = self.encoder(token)
        self.__password = password
        self.__host = host
        self.__user = user
        self.__port = port

    def __enter__(self) -> FTP:
        self.connect(self.__host, self.__port)
        self.login(self.__user, self.__password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
