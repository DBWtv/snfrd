from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^ftp_files/(?P<path>.*)$', views.index, name='ftp'),
]
