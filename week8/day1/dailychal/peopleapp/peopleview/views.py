from django.shortcuts import render

# Create your views here.

people = [
    {"id": 1, "name": "Bob Smith", "age": 35, "country": "USA"},
    {"id": 2, "name": "Martha Smith", "age": 60, "country": "USA"},
    {"id": 3, "name": "Fabio Alberto", "age": 18, "country": "Italy"},
    {"id": 4, "name": "Dietrich Stein", "age": 85, "country": "Germany"},
]

# function to render all the people in the people list


def peopleview(request):
    people = [
        {"id": 1, "name": "Bob Smith", "age": 35, "country": "USA"},
        {"id": 2, "name": "Martha Smith", "age": 60, "country": "USA"},
        {"id": 3, "name": "Fabio Alberto", "age": 18, "country": "Italy"},
        {"id": 4, "name": "Dietrich Stein", "age": 85, "country": "Germany"},
    ]
    return render(request, "allpeople.html", {"people": people})


# function to render a specific person in the people list by id


def peopleviewbyid(request, id):
    people = [
        {"id": 1, "name": "Bob Smith", "age": 35, "country": "USA"},
        {"id": 2, "name": "Martha Smith", "age": 60, "country": "USA"},
        {"id": 3, "name": "Fabio Alberto", "age": 18, "country": "Italy"},
        {"id": 4, "name": "Dietrich Stein", "age": 85, "country": "Germany"},
    ]
    for person in people:
        if person["id"] == id:
            return render(request, "person.html", {"person": person})
