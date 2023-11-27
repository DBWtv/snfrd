from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def run_ftp_server():
    authorize = DummyAuthorizer()

    authorize.add_user('user', '12345', '.', perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorize

    server = FTPServer(('127.0.0.1', 2121), handler)
    server.serve_forever()


if __name__ == '__main__':
    run_ftp_server()
