from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "rent/rental/",
        views.allrentals,
        name="allrentals"
        # add view function here
    ),
    path("rent/rental/<int:pk>/", views.rental, name="rental"),
    path("rent/rental/add/", views.add_rental, name="add_rental"),
    path("rent/customer/<int:pk>/", views.customer, name="customer"),
    path("rent/customer/", views.allcustomers, name="allcustomers"),
    path("rent/customer/add/", views.add_customer, name="add_customer"),
    path("rent/vehicles/", views.vehicle, name="allvehicles"),
    path("rent/vehicles/<int:pk>/", views.vehicle, name="vehicle"),
    path("faker", views.fakerentals, name="fakerentals"),
]


# /rent/rental/ - show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)

# /rent/rental/<pk> - show the information about the given rental:
# customer details
# vehicle details
# rental details (“Returned on: <date>” / “Not yet returned”)

# /rent/rental/add – provide a form to enter a customer ID and a vehicle ID to create a rental.
# If the customer or the vehicle does not exist, show a user-friendly error message.
# If the vehicle is currently being rented, show a relevant error message.

# /rent/customer/<pk> - show the customer matching the given ID

# /rent/customer/ - show all customers, in alphabetical order

# /rent/customer/add – provide a form to add a new customer

# /rent/vehicle/ - show all vehicles, grouped into their groups (‘bike’ and ‘scooter’)

# /rent/vehicle/<pk> - show the specific vehicle
# also show whether it’s currently being rented

# /rent/vehicle/add – provide a form to add a new vehicle.
