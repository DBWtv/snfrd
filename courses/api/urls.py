from django.urls import path
from . import views

urlpatterns = [
    path('api/add_row/', views.add_row_api, name='add_row_api'),
    path('api/enable_days/', views.enable_days, name='enable_days'),
    path('api/update_table/', views.update_table, name='update_table'),
    path('api/add_lecture/', views.add_lecture, name='add_lecture'),
    path('api/change_about/', views.change_title, name='change_about'),
    path('api/add_file/', views.add_file, name='add_file'),
    path('api/edit_lecture/', views.edit_lecture, name='edit_lecture'),
]
