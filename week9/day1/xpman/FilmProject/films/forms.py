# # forms file of the django project
# Create the forms : AddFilmForm and AddDirectorForm using models forms and director from models.py

import django.forms as forms
import films.models as models


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = "__all__"


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = "__all__"
