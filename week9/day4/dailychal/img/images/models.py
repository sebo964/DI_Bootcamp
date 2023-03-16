from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# model for storing the images uploaded by the user


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images")
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.image.name
