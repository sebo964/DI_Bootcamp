# login form using the django builtin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
