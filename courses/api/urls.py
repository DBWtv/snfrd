from django.urls import path
from . import views

urlpatterns = [
    path('api/add_row/', views.add_row_api, name='add_row_api'),
    path('api/enable_days/', views.enable_days, name='enable_days'),
    path('api/update_table/', views.update_table, name='update_table'),
]
