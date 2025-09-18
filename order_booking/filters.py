import django_filters
from django_filters import DateFilter, CharFilter, DateTimeFilter
from django.forms.widgets import DateInput
from django import forms

from store.models import *
from .forms import *

from django_filters import FilterSet, ChoiceFilter, NumberFilter
from users.models import *



class order_booking_filter(django_filters.FilterSet):

    order_id = django_filters.CharFilter(
        field_name='order_id',
        lookup_expr='exact',
        label='Order ID',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order ID'}),
    )

    project_id = django_filters.CharFilter(
        field_name='id',
        lookup_expr='exact',
        label='project ID',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'project ID'}),
    )

    customer = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
        field_name='customer',
        widget=forms.Select(attrs={'class': 'form-control select2', 'id': 'customer'}),
    )

    

    status = django_filters.ChoiceFilter(
            field_name='status',
        choices=order_booking.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Status"
    )

    
    from_DC_date = DateFilter(
        field_name="DC_date",
        lookup_expr='gte',
        label="DC Date From",
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    to_DC_date = DateFilter(
        field_name="DC_date",
        lookup_expr='lte',
        label="DC Date To",

        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    class Meta:
        model = project
        fields = ['customer', 'order_id', 'project_id', 'status']

        

       