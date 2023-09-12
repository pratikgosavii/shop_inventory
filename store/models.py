from django.db import models


from users.models import User
from datetime import datetime, timezone

import pytz
ist = pytz.timezone('Asia/Kolkata')






class godown(models.Model):

    name = models.CharField(max_length=120, unique=False)
    
    
    def __str__(self):
        return self.name


class customer(models.Model):

    name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    
    
    def __str__(self):
        return self.name

class employee(models.Model):

    name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    
    
    def __str__(self):
        return self.name

class cutter(models.Model):

    name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    
    
    def __str__(self):
        return self.name







class category(models.Model):

    name = models.CharField(max_length=120, unique=False)
    
    
    def __str__(self):
        return self.name




class size(models.Model):
    
    name = models.FloatField(default=0)

    def __str__(self):
        return str(self.name)

class thickness(models.Model):
    
    name = models.CharField(max_length=120, unique=False)

    def __str__(self):
        return self.name

class grade(models.Model):
    
    name = models.CharField(max_length=120, unique=False)

    def __str__(self):
        return self.name

class dealer(models.Model):

    name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    
    
    def __str__(self):
        return self.name


class item_code(models.Model):

    code = models.CharField(max_length=120, unique=False)
    
    
    def __str__(self):
        return self.code





class product(models.Model):

    size = models.ForeignKey(size, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    thickness = models.ForeignKey(thickness, on_delete=models.CASCADE)
    grade = models.ForeignKey(grade, on_delete=models.CASCADE)


    


class product_qr(models.Model):
    
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name = "project_material_re", null = True, blank = True)
    qr_code = models.ImageField(upload_to='static/qrcode/', height_field=None, width_field=None, max_length=None, null = True, blank = True)
    supplier = models.ForeignKey(dealer, on_delete=models.CASCADE, null = True, blank = True)
    is_fix = models.BooleanField(default=False)
    moved_to_scratch = models.BooleanField(default=False)
    moved_to_left_over = models.BooleanField(default=False)
    date_of_pur = models.DateField(auto_now_add=False, null = True, blank = True)
    uploaded_file = models.FileField(upload_to='media/uploads/', null = True, blank = True) 

     