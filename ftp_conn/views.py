from django.http import HttpResponse
from storages.backends.ftp import FTPStorage


def index(request, path):
    ftp = FTPStorage()
    file = ftp._open(name=path, mode='rb')
    return HttpResponse(file.read(), content_type=cont_type(path))


def cont_type(path):
    extension = path.split('.')[-1]

    content_types = {
        'txt': 'text/plain',
        'html': 'text/html',
        'css': 'text/css',
        'js': 'application/javascript',
        'json': 'application/json',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'bmp': 'image/bmp',
        'svg': 'image/svg+xml',
        'mp3': 'audio/mpeg',
        'ogg': 'audio/ogg',
        'wav': 'audio/wav',
        'mp4': 'video/mp4',
        'webm': 'video/webm',
        'pdf': 'application/pdf',
        'doc': 'application/msword',
        'docx': 'application/msword',
        'xls': 'application/vnd.ms-excel',
        'xlsx': 'application/vnd.ms-excel',
        'ppt': 'application/vnd.ms-powerpoint',
        'pptx': 'application/vnd.ms-powerpoint',
        'zip': 'application/zip',
        'tar': 'application/x-tar',
        'gz': 'application/gzip',
        'exe': 'application/octet-stream',
        'bin': 'application/octet-stream'
    }

    return content_types.get(extension, 'application/octet-stream')
