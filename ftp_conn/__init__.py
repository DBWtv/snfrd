from django.conf import settings
from .connection import FTPConnection


ftp = FTPConnection(
    token=settings.FTP_PASS_HASH_KEY,
    host=settings.FTP_HOST,
    port=settings.FTP_PORT,
    user=settings.FTP_USER,
    password=settings.FTP_PASSWORD
)
