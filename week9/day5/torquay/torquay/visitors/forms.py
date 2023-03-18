from django import forms
from .models import Booking, Contact, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["checkin", "checkout", "guests"]
        widgets = {
            "checkin": forms.DateInput(attrs={"type": "date"}),
            "checkout": forms.DateInput(attrs={"type": "date"}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]
        widgets = {
            "rating": forms.Select(
                choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
            )
        }
