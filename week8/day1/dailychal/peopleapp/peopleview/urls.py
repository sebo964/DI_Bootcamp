from django.urls import path, include
from . import views

urlpatterns = [
    path("people", views.peopleview, name="peopleview"),
    path("peopleview/<int:id>", views.peopleviewbyid, name="peopleview"),
]
