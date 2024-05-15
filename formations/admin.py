from django.contrib import admin
from .models import *

# Register your models here.

class AdminFormation(admin.ModelAdmin):
    list_display = ['titre', 'cout', 'duree', 'active']

admin.site.register(Formations, AdminFormation)
admin.site.register(Modules)
