from django.db import models

# Create your models here.

# Models:
# Customer
# first name
# last name
# email
# phone number
# address
# city
# country


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


# Vehicle
# vehicle type (foreign key to Vehicle Type model)
# date created
# real cost (how much it costs)
# size (foreign key to Vehicle Size model)


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_type


# Vehicle Type
# name


class VehicleType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Vehicle Size
# name


class VehicleSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Rental
# rental date
# return date
# customer (FK to Customer)
# vehicle (FK to Vehicle)


class Rental(models.Model):
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


# Rental Rate
# daily rate
# vehicle type (FK to Vehicle Type)
# vehicle size (FK to Vehicle Size)


class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_type
