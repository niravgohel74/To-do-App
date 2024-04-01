from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_todo, name="create_todo"),
    path('complete/<int:todo_id>/', complete_todo, name="complete_todo"),
    path('delete/<int:todo_id>/', delete_todo, name="delete_todo"),
]