import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from store.models import *
from .forms import *

from django_filters import FilterSet, ChoiceFilter, NumberFilter


class project_filter(django_filters.FilterSet):

    item_code = django_filters.ModelChoiceFilter(
        queryset=item_code.objects.all(),  # Replace with your actual ItemCode queryset
        field_name='project__project_material_re_1__project_material_re__project_matarial_qr_production__item_code',
        to_field_name='code',  # Field used to compare with the selected value
        label='Item Code',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

   
    customer = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
        field_name='project_material_re_1__employee_name',

        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'customer'
            })
    )
   
    from_DC_date = DateFilter(
        field_name="project_material_re_1__DC_date",  # Field name to filter on
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )
    
    to_DC_date = DateFilter(
        field_name="project_material_re_1__DC_date",  # Field name to filter on
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )


    class Meta:
        model = project_matarial_production
        fields = '__all__'
       