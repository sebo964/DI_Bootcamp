from django.shortcuts import render
from . import forms
from .models import Film, Director, Category, Country
from django.contrib.auth import login, authenticate


def homepage(request):
    films = Film.objects.all()
    return render(request, "homepage.html", {"homepage": films})


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


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "homepage.html")
    return render(request, "registration/register.html")


def login(request):
    if request.method == "POST":
        if authenticate(username="username", password="password"):
            return render(request, "homepage.html")
    return render(request, "registration/login.html")


def logout(request):
    if request.method == "POST":
        form = forms.LogoutForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "homepage.html")
    return render(request, "registration/logout.html")


def profile(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "homepage.html")
    return render(request, "registration/profile.html")


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
