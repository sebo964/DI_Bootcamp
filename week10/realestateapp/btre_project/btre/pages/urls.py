from django.urls import path
from . import views
from listings.views import index, listing, search

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("search.html", search, name="searchhome"),
]
