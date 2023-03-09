# # create a form that takes these values
#     title = models.CharField(max_length=255)
#     details = models.TextField()
#     has_been_done = models.BooleanField(default=False)
#     date_creation = models.DateTimeField(auto_now_add=True)
#     date_completion = models.DateTimeField(auto_now_add=True)
#     deadline_date = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category)

# in the form validate the fields to the same values as the model

from django import forms
from .models import Todo, Category
from django.core.validators import MinLengthValidator


class TodoForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    title = forms.CharField(max_length=255, validators=[MinLengthValidator(5)])

    details = forms.CharField(
        widget=forms.Textarea, validators=[MinLengthValidator(10)]
    )
    deadline_date = forms.DateField(widget=forms.DateInput(), required=False)

    class Meta:
        model = Todo
        fields = [
            "title",
            "details",
            "has_been_done",
            "deadline_date",
            "category",
        ]


class deleteForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["id"]
