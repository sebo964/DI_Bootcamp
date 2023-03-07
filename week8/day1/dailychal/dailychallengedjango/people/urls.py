from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.people_list, name='people_list'),
]
