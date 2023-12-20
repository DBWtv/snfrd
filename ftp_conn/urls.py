from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^ftp_files/(?P<path>.*)$', views.get_file, name='ftp'),
    re_path(r'^delete_file/(?P<path>.*)$', views.delete_file, name='ftp'),
]
