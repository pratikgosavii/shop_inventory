import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from .models import *
from .forms import *




class stock_filter(django_filters.FilterSet):

    company_goods = django_filters.ModelChoiceFilter(
        queryset=category.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'company'
            })
    )
   
    goods_company = django_filters.ModelChoiceFilter(
        queryset=size.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'company'
            })
    )

    dealer = django_filters.ModelChoiceFilter(
        queryset=dealer.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'company'
            })
    )

    total_bag = django_filters.NumberFilter(
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'company'
            })
    )
    

    class Meta:
        model = stock
        fields = '__all__'
       
   