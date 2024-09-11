import django_filters
from django_filters import DateFilter, CharFilter, DateTimeFilter
from django.forms.widgets import DateInput
from django import forms

from store.models import *
from .forms import *

from django_filters import FilterSet, ChoiceFilter, NumberFilter
from users.models import *

class project_filter(django_filters.FilterSet):

    item_code = django_filters.ModelChoiceFilter(
        queryset=item_code.objects.all(),  # Replace with your actual ItemCode queryset
        field_name='item_code',
        to_field_name='code',  # Field used to compare with the selected value
        label='Item Code',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

   
    customer = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
        field_name='customer',

        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'customer'
            })
    )
   
    from_DC_date = DateFilter(
        field_name="DC_date",  # Field name to filter on
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )
    
    to_DC_date = DateFilter(
        field_name="DC_date",  # Field name to filter on
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )


    class Meta:
        model = project
        fields = '__all__'
       


       

class project_matarial_production_filter(django_filters.FilterSet):

    item_code = django_filters.ModelChoiceFilter(
        queryset=item_code.objects.all(),  # Replace with your actual ItemCode queryset
        field_name='item_code',
        to_field_name='code',  # Field used to compare with the selected value
        label='Item Code',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

   
    project = django_filters.ModelChoiceFilter(
        queryset=project.objects.all(),
        field_name='project__customer__name',

        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'customer'
            })
    )
   
    from_date_time = DateTimeFilter(
        field_name="date_time",  # Field name in your model
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateTimeInput(attrs={
            'id': 'from_datepicker', 
            'type': 'datetime-local',  # Allows selection of both date and time
            'class': 'form-control date_css'  # Add custom CSS class if needed
        }),
        input_formats=['%Y-%m-%dT%H:%M']  # Match the format for datetime-local
    )
    
    to_date_time = DateTimeFilter(
        field_name="date_time",  # Field name in your model
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateTimeInput(attrs={
            'id': 'to_datepicker', 
            'type': 'datetime-local',  # Allows selection of both date and time
            'class': 'form-control date_css'  # Add custom CSS class if needed
        }),
        input_formats=['%Y-%m-%dT%H:%M']  # Match the format for datetime-local
    )




    class Meta:
        model = project_matarial_production
        fields = '__all__'
       


class project_inward_filter(django_filters.FilterSet):
   
    from_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )
    
    to_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )


    class Meta:
        model = project_inward
        fields = '__all__'



class project_outward_filter(django_filters.FilterSet):

   
    project = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
        field_name='project__order_id',

        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'project'
            })
    )
   
    customer = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
        field_name='customer__name',

        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'customer'
            })
    )
   
    from_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )
    
    to_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )


    class Meta:
        model = project_outward
        fields = '__all__'
       

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
    