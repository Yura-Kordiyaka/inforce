# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


class CustomUserAdmin(UserAdmin):
    model = Employee
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', 'phone_number')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'address', 'phone_number']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'address', 'phone_number']
    ordering = ['username']


admin.site.register(Employee, CustomUserAdmin)
