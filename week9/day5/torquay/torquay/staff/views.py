from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from visitors.models import Booking, Contact, Review


# Create your views here.

# login view that requests login credentials


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "staff/staffpage.html")
        else:
            return render(
                request, "staff/login.html", {"message": "Invalid credentials."}
            )

    return render(request, "staff/login.html")


def bookings_view(request):
    bookings = Booking.objects.all()
    contacts = Contact.objects.all()
    reviews = Review.objects.all()
    return render(
        request,
        "staff/staffpage.html",
        {"bookings": bookings},
        {"contacts": contacts},
        {"reviews": reviews},
    )


def booking_management_view(request):
    if request.method == "POST":
        # Handle form submission
        room_type = request.POST.get("room_type")
        checkin_date = request.POST.get("checkin_date")
        checkout_date = request.POST.get("checkout_date")
        guests = request.POST.get("guests")
        # Create new booking
        booking = Booking.objects.create(
            room_type=room_type,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            guests=guests,
        )
        # Redirect to bookings page
        return redirect("staffpage")
    else:
        # Render booking management form
        return render(request, "staff/staffpage.html")


def delete_review_view(request):
    if request.method == "POST":
        review_id = request.POST.get("review_id")
        review = Review.objects.get(id=review_id)
        review.delete()
        # Redirect to reviews page
        return redirect("reviews")
