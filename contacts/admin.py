from django.contrib import admin
from .models import Contacts, NewsLetters

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['nom', 'sujet', 'email']

admin.site.register(Contacts, ContactAdmin)
admin.site.register(NewsLetters)