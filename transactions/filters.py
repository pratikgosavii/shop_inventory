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

    

    item_code = django_filters.ModelChoiceFilter(
        queryset=item_code.objects.filter(status = True),
        field_name='item_code',
        to_field_name='code',
        label='Item Code',
        widget=forms.Select(attrs={'class': 'form-control select2'}),
    )

    
    from_DC_date = DateFilter(
        field_name="DC_date",
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    to_DC_date = DateFilter(
        field_name="DC_date",
        lookup_expr='lte',
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    class Meta:
        model = order_booking
        fields = ['item_code', 'customer', 'order_id', 'project_id']

        

class project_filter(django_filters.FilterSet):

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

    

    item_code = django_filters.ModelChoiceFilter(
        queryset=item_code.objects.filter(status = True),
        field_name='item_code',
        to_field_name='code',
        label='Item Code',
        widget=forms.Select(attrs={'class': 'form-control select2'}),
    )

    
    from_DC_date = DateFilter(
        field_name="DC_date",
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    to_DC_date = DateFilter(
        field_name="DC_date",
        lookup_expr='lte',
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    class Meta:
        model = project
        fields = ['item_code', 'customer', 'order_id', 'project_id']

        

       

class project_matarial_production_filter(django_filters.FilterSet):

    item_code = django_filters.ModelChoiceFilter(
        queryset=item_code.objects.filter(status = True),  # Replace with your actual ItemCode queryset
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
       

class product_qr_filter(django_filters.FilterSet):

    moved_to_scratch = django_filters.BooleanFilter(
        widget=forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
        label="Moved to Scratch"
    )

    moved_to_left_over = django_filters.BooleanFilter(
        widget=forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
        label="Moved to Left Over"
    )

    finish = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Finish"
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
    
    class Meta:
        model = product_qr
        fields = ['moved_to_scratch', 'moved_to_left_over', 'finish', 'status']



class ProjectOutwardMainLabelFilter(django_filters.FilterSet):
    # Filters for the main label's date_time
    from_main_label_date = django_filters.DateTimeFilter(
        field_name='date_time', lookup_expr='gte', label='From Main Label Date',
        widget=forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )
    to_main_label_date = django_filters.DateTimeFilter(
        field_name='date_time', lookup_expr='lte', label='To Main Label Date',
        widget=forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    # Filters for the small label's date_time
    from_small_label_date = django_filters.DateTimeFilter(
        method='filter_small_label_from_date', label='From Small Label Date',
        widget=forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )
    to_small_label_date = django_filters.DateTimeFilter(
        method='filter_small_label_to_date', label='To Small Label Date',
        widget=forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    class Meta:
        model = project_outward_main_label
        fields = ['from_main_label_date', 'to_main_label_date', 'from_small_label_date', 'to_small_label_date']

    def filter_small_label_from_date(self, queryset, name, value):
        """Filter main labels where related small labels have a date_time >= value."""
        return queryset.filter(main_label_re__date_time__gte=value)

    def filter_small_label_to_date(self, queryset, name, value):
        """Filter main labels where related small labels have a date_time <= value."""
        return queryset.filter(main_label_re__date_time__lte=value)