from .gif.models import Category

# Create four categories and add them to the database
categories = [
    Category(name="Funny", gif_ids=[1, 2, 3]),
    Category(name="Cute", gif_ids=[4, 5, 6]),
    Category(name="Scary", gif_ids=[7, 8, 9]),
    Category(name="Weird", gif_ids=[10]),
]
for category in categories:
    category.save()
