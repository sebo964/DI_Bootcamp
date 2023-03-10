# direct to the views file in the gif app

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
