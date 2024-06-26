from django.contrib import admin
from .models import Utilisateurs
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm


# Register your models here.

class AdminUser(UserAdmin):
    form = UserChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personnel Info', {
         'fields': ('first_name', 'last_name', 'email', 'telephone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions',)}),
        ('date important', {'fields': ('date_joined', 'last_login')})
    )

admin.site.register(Utilisateurs, AdminUser)