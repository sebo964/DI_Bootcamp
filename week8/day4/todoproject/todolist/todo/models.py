from django.db import models

# Create your models here.

# Create a Category Model with the fields :
# name
# image (for now a URL field - it can be also be an icon )


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    category_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


# Create a Todo Model with the fields :
# title
# details
# has_been_done : set by default to False
# date_creation (when the user created the todo)
# date_completion (when the user finished the todo)
# deadline_date (when the user has to finish the todo)
# category: One to Many relationship with the Category Model (ForeignKey)


# Note: A Todo can have one category, and a category can be shared among many todos.
# Example of category : work, home, shopping, studies, social


class Todo(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(default=None, null=True)
    deadline_date = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
