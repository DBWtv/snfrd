from django.urls import path
from . import views

urlpatterns = [
    path('api/add_row/', views.add_row_api, name='add_row_api'),
]
