from django.urls import path
from . import views
from .api.urls import urlpatterns as api_urls

urlpatterns = [
    path('<str:id>/', views.course, name='course'),
    path('<str:id>/edit/', views.course_admin, name='course_admin'),
]

urlpatterns += api_urls
