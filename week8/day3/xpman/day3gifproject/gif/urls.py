# direct to the views file in the gif app

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("like/<int:gif_id>/", views.like, name="like"),
    path("dislike/<int:gif_id>/", views.dislike, name="dislike"),
]
