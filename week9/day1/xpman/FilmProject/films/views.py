from django.shortcuts import render
from . import forms

# Create your views here.

# render homepage.html


def homepage(request):
    return render(request, "homepage.html")


# Create the views : addFilm and addDirector


def addFilm(request):
    if request.method == "POST":
        form = forms.AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "homepage.html")
    return render(request, "film/addFilm.html")


def addDirector(request):
    if request.method == "POST":
        form = forms.AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "homepage.html")
    return render(request, "director/adddirector.html")
