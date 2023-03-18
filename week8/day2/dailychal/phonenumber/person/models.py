from django.db import models

# from models.PhoneNumberField import PhoneNumberField

# # Create your models here.
# # id (Integer, Primary Key)
# name (String)
# email (String, unique)
# phone number (PhoneNumberField)
# address (String)


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
