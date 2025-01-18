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

            'DC_date': DateInput(attrs={ 'class': 'form-control dateclas', 'type': 'date'}, format = '%Y-%m-%d'),
            
        }



           
           

class project_Form(forms.ModelForm):



    class Meta:
        model = project
        fields = '__all__'
        widgets = {
           
            'employee_name': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee_name'
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
           
           
            'order_id': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'order_id'
            }),
           
            'rra_invoice_no': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'rra_invoice'
            }),

            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),


            # 'design_file': forms.ClearableFileInput(attrs={
            #                 'class': 'form-control',
            # }),

            # 'own_design_file': forms.ClearableFileInput(attrs={
            #                 'class': 'form-control',
                            
            # }),
           
          

            'DC_date': DateInput(attrs={ 'class': 'form-control dateclas', 'type': 'date'}, format = '%Y-%m-%d'),
            
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

class project_inward_Form(forms.ModelForm):
    class Meta:
        model = project_inward
        fields = '__all__'
        widgets = {
           



            'inward_item_code': forms.Select(attrs={
                'class': 'form-control sele', 'id': 'inward_item_code_id'
            }),

            'inward_supplier': forms.Select(attrs={
                'class': 'form-control sele', 'id': 'bag_size'
            }),

            'quantity': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),

            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),

          
            'date': DateInput(attrs={ 'class': 'form-control dateclas', 'type': 'date'}, format = '%Y-%m-%d'),

           
        }

class project_outward_Form(forms.ModelForm):
    class Meta:
        model = project_outward
        fields = '__all__'
        widgets = {
           
            'quantity': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'description'
            }),

            'project': forms.Select(attrs={
                'class': 'form-control', 'id': 'bag_size'
            }),

            'date': DateInput(attrs={ 'class': 'form-control dateclas', 'type': 'date'}, format = '%Y-%m-%d'),

           
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




class project_matarial_production_Form(forms.ModelForm):

    date_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control dateclas',
            'type': 'datetime-local'  # Allows both date and time input
        }),
    )


    class Meta:
        model = project_matarial_production
        fields = '__all__'
        widgets = {
           
            'item_code': forms.Select(attrs={
                'class': 'form-control', 'name' : 'item_code'
            }),



        }

        



class product_qr_Form(forms.ModelForm):

    uploaded_file = forms.FileField(label='Select a file', required=False)
    
    class Meta:
        model = product_qr
        fields = '__all__'
        widgets = {
          
           

            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'thickness'
            }),

            'finish': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'finish',
            }),


            'date_of_pur' : DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
          
            
        }




class inward_item_code_Form(forms.ModelForm):

    uploaded_file = forms.FileField(label='Select a file', required=False)
    
    class Meta:
        model = inward_item_code
        fields = '__all__'
        widgets = {
          
           

            'item_code': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'item_code'
            }),

            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description',
            }),


        }


