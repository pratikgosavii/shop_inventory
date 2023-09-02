from django import forms
from django.forms.widgets import DateInput

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class request_material_Form(forms.ModelForm):
    class Meta:
        model = request_material
        fields = '__all__'
        widgets = {
            'godown': forms.Select(attrs={
                'class': 'form-control', 'id': 'godown'
            }),
            'company': forms.Select(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'company_goods': forms.Select(attrs={
                'class': 'form-control', 'id': 'company_goods'
            }),
            'goods_company': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
            'employee_name': forms.Select(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),

            'customer_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),
           
           
            'bags': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),
            'DC_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'total_bag'
            }),

            'DC_date': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
            
        }



class project_Form(forms.ModelForm):
    class Meta:
        model = project
        fields = '__all__'
        widgets = {
           
            'employee_name': forms.Select(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
           
           
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
           
          

            'DC_date': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
            
        }



class project_matarial_Form(forms.ModelForm):
    class Meta:
        model = project_material
        fields = '__all__'
        widgets = {
           
            'quantity': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),

            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),

            'project': forms.Select(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),
           
        }

class project_matarial_qr_Form(forms.ModelForm):
    class Meta:
        model = project_matarial_qr
        fields = '__all__'
        widgets = {
           
            'item_code': forms.Select(attrs={
                'class': 'form-control', 'id': 'bag_size', 'name' : 'item_code'
            }),
            'production_quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'bag_size', 'name' : 'production_quantity'
            }),
            'cutter': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'bag_size', 'name' : 'cutter'
            }),


        }


class product_qr_Form(forms.ModelForm):
    class Meta:
        model = product_qr
        fields = '__all__'
        widgets = {
          

            'date_of_pur' : DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
          
           
            
        }




class goods_company_Form(forms.ModelForm):
    class Meta:
        model = stock
        fields = '__all__'
        widgets = {
         
            'company_goods': forms.Select(attrs={
                'class': 'form-control', 'id': 'company_goods'
            }),
           
            'goods_company_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),

            'total_bag': forms.NumberInput(attrs={
                'class': 'form-control cal', 'id': 'total_bag'
            }),
           
            
        }
