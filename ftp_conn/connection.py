from ftplib import FTP
from .services import Encoder # ENCODER
from django.conf import settings


class FTPConnection(FTP):
    encoder = Encoder

    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        port: int = 21,
        # encoder: Encoder = ENCODER,
    ):
        super().__init__()
        # self.encoder = encoder
        # TODO: pasword should be encrypted, when it is saved in the database
        self.__password = self.encoder.decrypt(password)
        self.__host = host
        self.__user = user
        self.__port = port

    def __enter__(self) -> FTP:
        self.connect(self.__host, self.__port)
        self.login(self.__user, self.__password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
