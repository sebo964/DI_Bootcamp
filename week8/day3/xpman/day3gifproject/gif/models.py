from django.db import models

# Create your models here.

# Create a Gif Model with the following fields :
# title (CharField)
# url (URLField)
# uploader_name (CharField)
# created_at (DatetimeField, should be populated when created).


class Gif(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploader_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    gif_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.AutoField(primary_key=True)
    gifs = models.ManyToManyField(Gif, related_name="category")

    def __str__(self):
        return self.name
