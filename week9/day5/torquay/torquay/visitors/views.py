from django.shortcuts import render, redirect
from .forms import BookingForm, ContactForm, ReviewForm


def success(request):
    return render(request, "success.html")


def visitor(request):
    booking_form = BookingForm()
    contact_form = ContactForm()
    review_form = ReviewForm()
    if request.method == "POST":
        if "booking_submit" in request.POST:
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save(commit=True)
                # do any additional processing or validation here
                booking.save()
                return redirect("success")
        elif "contact_submit" in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact = contact_form.save(commit=True)
                # do any additional processing or validation here
                contact.save()
                return redirect("success")
        elif "review_submit" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=True)
                # do any additional processing or validation here
                review.save()
                return redirect("success")
    context = {
        "booking_form": booking_form,
        "contact_form": contact_form,
        "review_form": review_form,
    }
    return render(request, "visitor.html", context)
