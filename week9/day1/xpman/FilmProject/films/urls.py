# redirect to views in the films app

from django.urls import path
from . import views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("homepage.html", views.homepage, name=""),
    path("film/addfilm.html", views.addFilm),
    path("director/adddirector.html", views.addDirector),
    path("registration/register.html", views.register),
    path("registration/login.html", views.login),
    path("registration/logout.html", views.logout),
    path("registration/signup.html", views.signup),
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
