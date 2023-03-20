from django.shortcuts import render
from .models import Person
from django.contrib.auth.models import User

# Create your views here.


def personphone(request, phonenumber):
    person = Person.objects.get(phone_number=phonenumber)
    print(Person.phone_number)
    return render(request, "personphonedetails.html", {"person": person})


def personname(request, name):
    person = Person.objects.get(name=name)
    print(Person.name)
    return render(request, "personphonedetails.html", {"person": person})


def people(request):
    people = Person.objects.all()
    print(Person.name[1])
    return render(request, "personphonedetails.html", {"person": people})
