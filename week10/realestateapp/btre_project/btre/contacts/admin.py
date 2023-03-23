from django.contrib import admin
from .models import Contact 
# Register your models here.

from django.apps import apps

class ContactAdmin(Contact):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25
    list_filter = ('contact_date',)
    
admin.site.register(Contact, ContactAdmin)
    