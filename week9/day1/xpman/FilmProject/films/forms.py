# # forms file of the django project
# Create the forms : AddFilmForm and AddDirectorForm using models forms and director from models.py

import django.forms as forms
import films.models as models
import django.contrib.auth.models as auth_models


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = "__all__"


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = "__all__"


class RegisterForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = "__all__"


class SignupForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = "__all__"


class LogoutForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = "__all__"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = "__all__"
