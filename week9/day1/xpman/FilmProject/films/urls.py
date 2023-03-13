# redirect to views in the films app

from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("film/addfilm", views.addFilm, name="addFilm"),
    path("director/addfirector", views.addDirector, name="addDirector"),
]
