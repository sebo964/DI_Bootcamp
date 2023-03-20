from django.shortcuts import render

# from .models import Animal, Family

# Create your views here.

# from the models there are class Animals and family

# # Create 3 views, corresponding to the following URLs:
# /family/X, where X is the ID (primary key) of the given family. Should show a list of all animals in that family.
# /animal/X, where X is the ID (primary key) of the given animal. Should show all the information about the given animal.
# /animals/ - should show a list of all the animals. When you click on any of the animals in the list, you should be taken to /animal/X (see above).


animals_main = {
    "animals": [
        {
            "id": 1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height": 4.2,
            "speed": 34,
            "family": 2,
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height": 4.2,
            "speed": 34,
            "family": 1,
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height": 4.2,
            "speed": 34,
            "family": 1,
        },
    ],
    "families": [{"id": 1, "name": "Felidae"}, {"id": 2, "name": "Caninae"}],
}


def all_animals(request):
    # animals = animals_main["animals"]
    animals = animals_main["animals"]
    return render(request, "all_animals.html", {"animals": animals})


def animal(request, animal_id):
    animals = animals_main["animals"]
    for animal in animals:
        if animal["id"] == animal_id:
            return render(request, "animals.html", {"animal": animal})


def family(request, family_id):
    for family in animals_main["families"]:
        if family["id"] == family_id:
            return render(request, "family.html", {"family": family})
