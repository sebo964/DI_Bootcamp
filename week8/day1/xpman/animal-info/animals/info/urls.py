from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.all_animals, name="all_animals_html_page"),
    path("info/<int:animal_id>", views.animal, name="animals_html_page"),
    path("info/family/<int:family_id>", views.family, name="family_html_page"),
]
