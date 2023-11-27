from ftplib import FTP

host = '127.0.0.1'
port = 2121
user = 'user'
password = '12345'


class FTPConnection(FTP):

    def __init__(self, host: str, port: int, user: str, password: str):
        super().__init__()
        self.connect(host, port)
        self.login(user, password)
        self.cwd('.')
