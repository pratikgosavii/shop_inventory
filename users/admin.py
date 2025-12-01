from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm  # Import your custom forms

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Use the custom form for user creation
    form = CustomUserChangeForm  # Use the custom change form
    change_password_form = AdminPasswordChangeForm  # Ensure password change form is available
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_accounts', 'is_admin', 'is_reception', 'is_designer', 'is_cutter', 'is_salesman', 'is_planner', 'is_executor', 'is_order_booker')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_accounts', 'is_admin', 'is_reception', 'is_designer', 'is_cutter', 'is_salesman', 'is_planner', 'is_executor', 'is_order_booker', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'is_accounts', 'is_admin', 'is_reception', 'is_designer', 'is_cutter', 'is_salesman', 'is_planner', 'is_executor', 'is_order_booker')}
        ),
    )

# Register your custom admin class for the User model
admin.site.register(User, CustomUserAdmin)
