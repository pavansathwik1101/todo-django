from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_member/', add_member, name='add_member'),
    path('delete_member/<int:member_id>/', delete_member, name='delete_member'),
]
