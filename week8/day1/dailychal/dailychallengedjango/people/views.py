from django.shortcuts import render

# Create your views here.

#  add this dictionary to view
# people = [
#     {
#         'id': 1,
#         'name': 'Bob Smith',
#         'age': 35,
#         'country': 'USA'
#     },
#     {
#         'id': 2,
#         'name': 'Martha Smith',
#         'age': 60,
#         'country': 'USA'
#     },
#     {
#         'id': 3,
#         'name': 'Fabio Alberto',
#         'age': 18,
#         'country': 'Italy'
#     },
#     {
#         'id': 4,
#         'name': 'Dietrich Stein',
#         'age': 85,
#         'country': 'Germany'
#     }
# ]

from django.shortcuts import render


def people_list(request):
    people = {
        {
            'id': 1,
            'name': 'Bob Smith',
            'age': 35,
            'country': 'USA'
        },
        {
            'id': 2,
            'name': 'Martha Smith',
            'age': 60,
            'country': 'USA'
        },
        {
            'id': 3,
            'name': 'Fabio Alberto',
            'age': 18,
            'country': 'Italy'
        },
        {
            'id': 4,
            'name': 'Dietrich Stein',
            'age': 85,
            'country': 'Germany'
        }
    }
    context = {'people': people}

    return render(request, 'people.html', context)
