from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_staff']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)})
    )
admin.site.register(CustomUser, CustomUserAdmin)
