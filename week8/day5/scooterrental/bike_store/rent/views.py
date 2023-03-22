from django.shortcuts import render
from .models import Rental, Customer, Vehicle, VehicleType, VehicleSize
from django.http import HttpResponse
from faker import Faker
import random
from datetime import datetime, timedelta

# Create your views here.

# show a list of all rentals, unreturned first, then ordered by date ascending (earliest first) from the model Rental show them on allrentals.html.


def allrentals(request):
    rentals = Rental.objects.all()
    return render(request, "allrentals.html", {"rentals": rentals})


# /rent/rental/<pk> - show the information about the given rental:
# customer details
# vehicle details
# rental details (“Returned on: <date>” / “Not yet returned”)


def rental(request, pk):
    rental = Rental.objects.get(pk=pk)
    return render(request, "rental.html", {"rental": rental})


# /rent/rental/add – provide a form to enter a customer ID and a vehicle ID to create a rental.
# If the customer or the vehicle does not exist, show a user-friendly error message.
# If the vehicle is currently being rented, show a relevant error message.


def add_rental(request):
    if request.method == "POST":
        customer_id = request.POST["customer_id"]
        vehicle_id = request.POST["vehicle_id"]
        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            return render(
                request, "add_rental.html", {"error": "Customer does not exist"}
            )
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            return render(
                request, "add_rental.html", {"error": "Vehicle does not exist"}
            )
        if vehicle.rental_set.all():
            return render(
                request, "add_rental.html", {"error": "Vehicle is already rented"}
            )
        rental_date = request.POST["rental_date"]
        return_date = request.POST["return_date"]

        rental = Rental.objects.create(
            customer=customer,
            vehicle=vehicle,
            rental_date=rental_date,
            return_date=return_date,
        )
        return render(request, "rental.html", {"rental": rental})
    return render(request, "add_rental.html")


def customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, "customer.html", {"customer": customer})


def allcustomers(request):
    customers = Customer.objects.all()
    # sort the customer list by first name
    customers = sorted(customers, key=lambda customer: customer.first_name)
    return render(request, "allcustomers.html", {"customers": customers})


def add_customer(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]
        city = request.POST["city"]
        country = request.POST["country"]
        customer = Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            country=country,
        )
        # save the customer and redirect to the customer details page
        customer.save()
        return render(request, "allcustomers.html", {"customer": customer})
    return render(request, "add_customer.html")


def vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    # show rental details if the vehicle is rented
    # if not rented show a message that the vehicle is not rented
    if vehicle.rental_set.all():
        rental = vehicle.rental_set.all()[0]
        return render(request, "vehicle.html", {"vehicle": vehicle, "rental": rental})
    return render(request, "vehicle.html", {"vehicle": vehicle})


def allvehicles(request):
    vehicles = Vehicle.objects.all()
    # group the vehicles by type
    vehicles = sorted(vehicles, key=lambda vehicle: vehicle.type)
    return render(request, "allvehicles.html", {"vehicles": vehicles})


def add_vehicle(request):
    if request.method == "POST":
        vehicle_type_name = request.POST.get("vehicle_type_name")
        vehicle_size_name = request.POST.get("vehicle_size_name")
        real_cost = request.POST.get("real_cost")

        # Check if vehicle type exists
        try:
            vehicle_type = VehicleType.objects.get(name=vehicle_type_name)
        except VehicleType.DoesNotExist:
            return HttpResponse("Error: Vehicle type does not exist")

        # Check if vehicle size exists
        try:
            vehicle_size = VehicleSize.objects.get(name=vehicle_size_name)
        except VehicleSize.DoesNotExist:
            return HttpResponse("Error: Vehicle size does not exist")

        # Create new vehicle
        new_vehicle = Vehicle(
            vehicle_type=vehicle_type, size=vehicle_size, real_cost=real_cost
        )
        new_vehicle.save()

        return HttpResponse("Vehicle added successfully")

    else:
        # Render form to add new vehicle
        vehicle_types = VehicleType.objects.all()
        vehicle_sizes = VehicleSize.objects.all()
        context = {"vehicle_types": vehicle_types, "vehicle_sizes": vehicle_sizes}
        return render(request, "add_vehicle.html", context)


# Create 100 rentals using Faker. Use random data, but pay attention to the following:
# return date should sometimes be null
# return date (if not null) must be after rental date
# neither of these dates may be in the future
# if a vehicle is already rented and has not been returned, it should not be used for a new rental.


def fakerentals(request):
    fake = Faker()
    rentals = Rental.objects.all()
    vehicles = Vehicle.objects.all()
    customers = Customer.objects.all()
    for i in range(100):
        rental_date = fake.date_time_between(start_date="-1y", end_date="now")
        return_date = fake.date_time_between(start_date=rental_date, end_date="now")
        rental = Rental.objects.create(
            customer=random.choice(customers),
            vehicle=random.choice(vehicles),
            rental_date=rental_date,
            return_date=return_date,
        )
    return HttpResponse("100 fake rentals created")
