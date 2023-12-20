from django.shortcuts import render
from django.http import HttpResponse
from .connection import FTPConnection
from .models import FTPServer

from storages.backends.ftp import FTPStorage


def index(request, path):
    ftp = FTPStorage()
    file = ftp._open(name=path, mode='rb')
    return HttpResponse(file.read(), content_type=cont_type(path))


def cont_type(path):
    extension = path.split('.')[-1]

    content_types = {
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'svg': 'image/svg+xml',
        'webp': 'image/webp',
        'doc': 'application/msword',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'xls': 'application/vnd.ms-excel',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'ppt': 'application/vnd.ms-powerpoint',
        'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        # Добавьте другие расширения и их Content-Type по необходимости
    }

    return content_types.get(extension, 'application/octet-stream')
