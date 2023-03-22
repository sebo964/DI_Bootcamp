from django.urls import path
from . import views

urlpatterns = [
    path("realtors", views.realtor, name="realtor"),
]