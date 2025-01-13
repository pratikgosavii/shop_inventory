import django_filters
from django_filters import DateFilter, CharFilter, DateTimeFilter
from django.forms.widgets import DateInput
from django import forms

from store.models import *
from .forms import *

from django_filters import FilterSet, ChoiceFilter, NumberFilter
from users.models import *

class order_filter(django_filters.FilterSet):

    customer = django_filters.ModelChoiceFilter(
        queryset=sales_customer.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'customer'
            })
    )

    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user'
            })
    )

   
    date_start = DateFilter(field_name="date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    date_end = DateFilter(field_name="date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))
