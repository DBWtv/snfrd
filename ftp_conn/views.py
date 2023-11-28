from django.shortcuts import render
from django.http import HttpResponse
from . import ftp


def index(request):
    with ftp as f:
        respons = f.nlst()
    return HttpResponse(content=respons, content_type='text/plain')
