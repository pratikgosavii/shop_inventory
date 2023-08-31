from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

        
class godown_Form(forms.ModelForm):
    class Meta:
        model = godown
        
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }
        
class item_code_Form(forms.ModelForm):
    class Meta:
        model = item_code
        
        fields = ['code']
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'code'
            }),
            
        }


class category_Form(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
           
     
            
        }

class dealer_Form(forms.ModelForm):
    class Meta:
        model = dealer
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
           
     
            
        }

class customer_Form(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
           
     
            
        }

class employee_Form(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
           
     
            
        }




class size_Form(forms.ModelForm):
    class Meta:
        model = size
        fields = '__all__'
        widgets = {
          
          
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
           
            
        }

from django.forms.widgets import DateInput


class product_Form(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
        widgets = {
          
          
            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
          
            'size': forms.Select(attrs={
                'class': 'form-control', 'id': 'size'
            }),
          
            'thickness': forms.Select(attrs={
                'class': 'form-control', 'id': 'thickness'
            }),
          
            'grade': forms.Select(attrs={
                'class': 'form-control', 'id': 'grade'
            }),

           
            
        }



        

class thickness_Form(forms.ModelForm):
    class Meta:
        model = thickness
        fields = '__all__'
        widgets = {
          
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
           
            
        }

class grade_Form(forms.ModelForm):
    class Meta:
        model = grade
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
           
            
        }


