from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("homepage", views.homepage, name="index"),
    path("login/", views.login_view, name="login"),
    path("upload/", views.upload, name="upload"),
    path("accounts/", include("django.contrib.auth.urls")),
]
