from django.db import models

# # Create your models here.
# Create 4 new models :
# Country :
# name

# Category :
# name

# Film:
# title
# release_date (default the date of today)
# created_in_country : One to Many relationship with Country (the “nationality of the film”)
# available_in_countries : Many to Many relationship with Country
# category: Many to Many relationship with Category
# director : Many to Many relationship with Director

# Director:
# first_name
# last_name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(
        Country, related_name="available_in_countries"
    )
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __str__(self):
        return self.title
