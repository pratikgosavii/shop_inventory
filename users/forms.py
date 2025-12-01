from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User  # Import your User model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_accounts', 'is_admin', 'is_reception', 'is_designer', 'is_cutter')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_accounts',
            'is_admin',
            'is_reception',
            'is_designer',
            'is_cutter',
            'is_salesman',
            'is_planner',
            'is_executor',
            'is_order_booker',
            'groups',
            'user_permissions',
        )
