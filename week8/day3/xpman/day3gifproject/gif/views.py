# Create your views here.

#   Create a view that will render the index.html template which will display all the gifs in the database and the associated categories for each gif.


from django.shortcuts import render
from .models import Gif, Category


def index(request):
    gifs = Gif.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {"gifs": gifs, "categories": categories})
