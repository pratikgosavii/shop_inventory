from django import forms
from django.forms.widgets import DateInput

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class order_booking_Form(forms.ModelForm):

    order_id = forms.CharField(
        label="Purchase Order No",   # <-- custom label here
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Purchase Order No'}
        )
    )
     
    class Meta:
        model = order_booking
        fields = '__all__'
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control select2', 'id': 'customer', 'data-placeholder': 'Select Customer'
            }),
           
            'order_type': forms.Select(attrs={
                'class': 'form-control select2', 'id': 'order_type', 'data-placeholder': 'Select Order Type'
            }),
            'delivery_type': forms.Select(attrs={
                'class': 'form-control select2', 'id': 'delivery_type', 'data-placeholder': 'Select Delivery Type'
            }),
            'delivery_date': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format='%Y-%m-%d'),
            
            'expected_film_delivery_date': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format='%Y-%m-%d'),
            
            'date': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format='%Y-%m-%d'),
            
            'design_completion_expected_date': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format='%Y-%m-%d'),
            'status': forms.Select(attrs={
                'class': 'form-control select2', 'data-placeholder': 'Select Status'
            }),
            
        

            'is_drawing_avaiable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_flim_avaiable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        # extract user from kwargs
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # if user is designer → lock all except 3
        if user and getattr(user, "is_designer", False):
            editable_fields = [
                'expected_film_delivery_date',
                'is_drawing_avaiable',
                'is_flim_avaiable',
                'design_completion_expected_date',
            ]
            for field_name, field in self.fields.items():
                if field_name not in editable_fields:
                    field.disabled = True   # makes them non-editable


class production_orders_Form(forms.ModelForm):
    class Meta:
        model = production_orders
        fields = "__all__"
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "expected_end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # 👈 catch user passed from view
        super().__init__(*args, **kwargs)

        # Apply Bootstrap form-control to all fields
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-check-input'})

        # 👇 Only disable fields if user is executor
        if user and getattr(user, "is_executor", False):
            for field in self.fields.values():
                field.disabled = True

            # Enable only these
            self.fields['assigned_employees'].disabled = False
            self.fields['expected_end_date'].disabled = False
            self.fields['hold_reason'].disabled = False
            self.fields['remarks'].disabled = False