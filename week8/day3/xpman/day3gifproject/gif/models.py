from django.db import models


class Gif(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploader_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    gif_id = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.AutoField(primary_key=True)
    gifs = models.ManyToManyField(Gif, related_name="categories")

    def __str__(self):
        return self.name
