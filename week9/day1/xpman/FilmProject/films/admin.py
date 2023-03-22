from django.contrib import admin
from .models import Film, Director, Category, Country

# Register your models here.

# add app to the admin site

admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Category)
admin.site.register(Country)
