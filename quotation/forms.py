from django import forms
from django.forms.widgets import DateInput

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class order_Form(forms.ModelForm):

    class Meta:
        model = order
        fields = '__all__'
        widgets = {
          
           
            'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer',
            }),

            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description',
            }),

            'urgency': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'urgency',
            }),

            'requirements': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'requirements',
            }),

            'invoice': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'invoice',
            }),

            'rejection_reason': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'rejection_reason',
            }),

            'edit_explanation': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'edit_explanation',
            }),



            'date' : DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
          
            
        }



class OrderChildForm(forms.ModelForm):
    class Meta:
        model = order_child
        fields = '__all__'



        
class sales_customer_Form(forms.ModelForm):
    class Meta:
        model = sales_customer
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'mobile_no'
            }),
            'client_gst': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'client_gst'
            }),
            
           
     
            
        }



        
class color_Form(forms.ModelForm):
    class Meta:
        model = color
        
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }

        
class etching_Form(forms.ModelForm):
    class Meta:
        model = etching
        
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }

        
class text_matter_Form(forms.ModelForm):
    class Meta:
        model = text_matter
        
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }
        
class process_Form(forms.ModelForm):
    class Meta:
        model = process
        
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }



from django import forms
from .models import PSI

class PSIForm(forms.ModelForm):
    class Meta:
        model = PSI
        fields = ['etching', 'category', 'thickness', 'color', 'text_matter', 'process', 'range_576', 'range_720_1728', 'range_1872_2880', 'range_3024_4032', 'range_4608']



