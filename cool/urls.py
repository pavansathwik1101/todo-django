from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [ 
    path('', cool, name='cool'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('index/', index, name='index'),  # Add a separate URL for the main TODO page
    path('add_task/', add_task, name='add_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
