from django.contrib import admin

# Register your models here.
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(Rental)
admin.site.register(RentalRate)
