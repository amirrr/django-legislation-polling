from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
# from django.contrib.auth.admin import UserAdmin

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('phone_number', 'full_name', 'city', 'email', 'date_joined', 'phone_number_verified', 'is_staff', 'is_active', 'is_admin', 'is_superuser')
    search_fields = ('phone_number', 'full_name', 'city', 'email', 'date_joined')
    readonly_fields = ('date_joined',)

    ordering = ()
    list_filter = ()
    filter_horizontal = ()
    
    fieldsets = (
        (None, {'fields': ('phone_number', 'phone_number_verified', 'verification_code', 'date_joined', 'password')}),
        ('Personal info', {'fields': ('email', 'full_name', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_superuser')}),
    )
 



admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

