from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Image


def homepage(request):
    images = Image.objects.order_by("-timestamp")
    return render(request, "index.html", {"images": images})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("upload")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=True)
            image.user = request.user
            image.description = form.cleaned_data["description"]
            image.save(commit=True)
            return redirect("index")
    else:
        form = ImageForm()
    return render(request, "upload.html", {"form": form})
