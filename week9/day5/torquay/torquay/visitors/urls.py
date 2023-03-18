from django.urls import path
from . import views
from staff import views as staff_views

urlpatterns = [
    path("visitor", views.visitor, name="homepage"),
    path("", views.visitor, name="visitor"),
    path("login", staff_views.login_view, name="stafflogin"),
    # path("visitor/<int:id>", views.visitor, name="visitor"),
]
