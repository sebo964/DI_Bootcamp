from django.db import models
import random

# Create your models here.
# we assume there are 10 rooms in the hotel
# each room are the same so users cannot choose which room they want, it is assingned randomly


class Booking(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.PositiveIntegerField()
    room_booked = models.IntegerField(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


class Review(models.Model):
    rating = models.PositiveIntegerField(
        choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
    )
    comment = models.TextField()


# room availabity, stores the room number and the date it is booked, it links to the booking model
