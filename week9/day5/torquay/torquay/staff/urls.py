from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from visitors import views as visitor_views


urlpatterns = [
    path("login", views.login_view, name="stafflogin"),
    path("staffpage", views.login_view, name="staffpage"),
    path("", visitor_views.visitor, name="visitor"),
]
