from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/', views.course, name='course'),
    path('<str:id>/admin/', views.course_admin, name='course_admin'),
]
