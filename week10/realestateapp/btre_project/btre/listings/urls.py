from django.urls import path
from . import views

urlpatterns = [
    path("<int:listing_id>/listing", views.listing, name="listing"),
    path("", views.index, name="listings"),
    path("search", views.search, name="search"),
]

