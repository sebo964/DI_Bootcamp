from django.db import models

# Create your models here.
# # Realtor
# id
# name: STR
# photo: STR
# description: TEXT
# email: STR
# phone: STR
# is_MVP: bool (0)
# hire_date: DATE

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
