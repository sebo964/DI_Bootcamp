from .models import Image
from django.contrib.auth.models import User

import django.forms as forms
import django.contrib.auth.models as auth_models


# form to upload an image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "description"]
