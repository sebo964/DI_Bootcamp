from django import forms
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "city",
            "country",
        ]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["vehicle_type", "size", "real_cost"]

    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ["rental_date", "return_date", "customer", "vehicle"]

    rental_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
    return_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all())
