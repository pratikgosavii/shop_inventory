from django.db import models
from django.dispatch import receiver

# Create your models here.



from users.models import User
from datetime import datetime, timezone
from store.models import *



class request_material(models.Model):

    category = models.ForeignKey(category , on_delete=models.CASCADE, related_name='dscdc')
    size = models.ForeignKey(size , on_delete=models.CASCADE, related_name='sdcdscd')
    employee_name = models.CharField(max_length=50, null = True, blank = True)
    bags = models.BigIntegerField()
    customer_name = models.ForeignKey(customer , on_delete=models.CASCADE, related_name='dscdc')
    DC_number = models.CharField(max_length=50)
    DC_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.category.name

class project(models.Model):

    customer = models.ForeignKey(customer , on_delete=models.CASCADE, related_name='hfghjgjvhj')
    employee_name = models.ForeignKey(employee , on_delete=models.CASCADE, null=True, blank=True, related_name='dfsdds')
    DC_date = models.DateField(auto_now_add=False)
    description = models.CharField( max_length=50)
    order_id = models.CharField(unique=True, max_length=50)
    completed = models.BooleanField(default=False)
    # design_file = models.FileField(upload_to='media/project_design/')
    # own_design_file = models.FileField(upload_to='media/project_design/', blank=True)

    def __str__(self):
        return self.description
    
class sheets_rifd(models.Model):

    project_id = models.CharField( max_length=50)
    sheet_id = models.CharField(max_length=50)
    rfid_value = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

class sheet_tracking_history(models.Model):

    project_id = models.CharField( max_length=50)
    sheet_id = models.CharField(max_length=50)
    rfid_value = models.CharField(max_length=50)
    check_point = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    
class project_logs(models.Model):

    project = models.ForeignKey(project , on_delete=models.CASCADE, related_name='project_logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    field_name = models.CharField(max_length=255)
    old_value = models.TextField()
    new_value = models.TextField()

    def __str__(self):
        return self.project


class project_sheets_logs(models.Model):

    project = models.ForeignKey(project , on_delete=models.CASCADE, related_name='sdcdcsx')
    description = models.CharField( max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project

   
class project_material(models.Model):

    sheet_no = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name = "product_re")
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name = "project_material_re_1")
    

class project_matarial_qr(models.Model):
    
    project_material = models.ForeignKey(project_material, on_delete=models.CASCADE, related_name = "project_material_re", null = True, blank = True)
    product_qr =  models.ForeignKey(product_qr, on_delete=models.CASCADE, null = True, blank = True, related_name = "product_qr_pro")
    is_cutting_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.project_material.product.category.name

class project_matarial_production(models.Model):

    item_code = models.ForeignKey(item_code, on_delete=models.CASCADE, related_name = "item_code_re_1", null = True, blank = True)
    production_quantity = models.IntegerField(null = True, blank = True)
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name = "project_production_n")
    


from store.models import * 

class material_history(models.Model):

    product_qr = models.ForeignKey(product_qr, on_delete=models.CASCADE, related_name = "fdthfh")
    previous_size =  models.ForeignKey(size, on_delete=models.CASCADE, related_name = "sdsdsc")
    used_size =  models.ForeignKey(size, on_delete=models.CASCADE, related_name = "fscswdcscdthfh")
    left_size =  models.ForeignKey(size, on_delete=models.CASCADE, related_name = "fdsfcsfcscthfh")
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name = "project_n")
    cutter =  models.ForeignKey(cutter, on_delete=models.CASCADE, null = True, blank = True)



class stock(models.Model):

    quantity = models.BigIntegerField(default = 0, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    

class left_over_stock(models.Model):

    quantity = models.BigIntegerField(default = 0, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

class demo(models.Model):

    name = models.CharField(max_length=50)
    

class scratch_stock(models.Model):

    quantity = models.BigIntegerField(default = 0, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    


class order(models.Model):
    
    customer = models.TextField()
    description = models.TextField()
    urgency = models.TextField()
    requirements = models.TextField()
    invoice = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    is_reported = models.BooleanField(default=False)



# models.py
from django.db import models
from django.contrib.auth.models import User
# alerts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class alert(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class notification_table(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_reported = models.BooleanField(default=False)

