from django.http import HttpResponse
from storages.backends.ftp import FTPStorage
from courses.models import Attachment
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt


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


@require_GET
def get_file(request, path):
    with FTPStorage()._open(name=path, mode='rb') as file:
        return HttpResponse(file.read(), content_type=cont_type(path))


@csrf_exempt
@require_POST
def delete_file(request, path):
    file = Attachment.objects.get(file=path)
    file.delete()
    return HttpResponse(status=204)
