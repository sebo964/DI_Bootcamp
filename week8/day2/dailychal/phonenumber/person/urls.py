from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("name/<name>", views.personname, name="person"),
    path("num/<int:phonenumber>", views.personphone, name="person"),
    path("people/", views.people, name="people"),
]
