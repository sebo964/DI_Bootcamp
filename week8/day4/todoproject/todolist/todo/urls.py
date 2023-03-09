from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.todolist, name="index"),
    path("add", views.todo_add, name="add"),
    path("todolist", views.todolist, name="todolist"),
    path("complete_todo", views.complete_todo, name="todo_view"),
]
