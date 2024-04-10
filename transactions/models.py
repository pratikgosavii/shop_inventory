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
    
    customer = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    urgency = models.TextField(null = True, blank = True)
    requirements = models.TextField(null = True, blank = True)
    invoice = models.IntegerField(null = True, blank = True)
    date = models.DateTimeField(null = True, blank = True)
    order_id = models.IntegerField()




MATERIAL_OPTION_CHOICES = (
        ('ss_304', 'ss_304'),
        ('ss_316', 'ss_316'), 
        ('ss_316_L', 'ss_316_L'),
        ('aluminium_coil', 'aluminium_coil'),
        ('sheet_2S', 'sheet_2S'),
        ('brass', 'brass'),
        ('copper', 'copper'),
        ('mild_sheel', 'mild_sheel'),
        ('spring_sheel', 'spring_sheel'),
        ('nickel', 'nickel'),
        ('beryllium_copper', 'beryllium_copper'),
        ('trifoliate_sandwich', 'trifoliate_sandwich'),
        ('any_other_please_mention', 'any_other_please_mention'),
    )

PROCESS_OPTION_CHOICES = (
        ('chemical_etching', 'chemical_etching'),
        ('etching_laser_cutting', 'etching_laser_cutting'),
        ('etching_laser_engraving', 'etching_laser_engraving'),
        ('chemical_milling', 'chemical_milling'),
        ('anodic_print', 'anodic_print'),
        ('laser_cutting', 'laser_cutting'),
        ('laser_cutting_coating', 'laser_cutting_coating'),
        ('stamping', 'stamping'),
        ('injection_mould_texturing', 'injection_mould_texturing'),
    )

SQINCH_OPTION_CHOICES = (

('144', '144'),
('288', '288'),
('432', '432'),
('576' ,'576'),
('720' ,'720'),
('864' ,'864'),
('1008' ,'1008'),
('1152' ,'1152'),
('1296' ,'1296'),
('1440' ,'1440'),
('1584' ,'1584'),
('1728' ,'1728'),
('1872' ,'1872'),
('2016' ,'2016'),
('2160' ,'2160'),
('2304' ,'2304'),
('2448' ,'2448'),
('2592' ,'2592'),
('2736' ,'2736'),
('2880' ,'2880'),
('3024' ,'3024'),
('3168' ,'3168'),
('3312' ,'3312'),
('3456' ,'3456'),
('3600' ,'3600'),
('3744' ,'3744'),
('3888' ,'3888'),
('4032' ,'4032'),
('4176' ,'4176'),
('4320' ,'4320'),
('4464' ,'4464'),
('4608' ,'4608'),
)



TEXT_MATTER_OPTION_CHOICES = (

('standard_text_matter', 'standard_text_matter'),
('variable_text_matter', 'variable_text_matter'),

)

ETCHING_OPTION_CHOICES = (

('deep_etching', 'deep_etching'),
('embossed_etching', 'embossed_etching'),

)

ETCHING_OPTION_CHOICES = (

('deep_etching', 'deep_etching'),
('embossed_etching', 'embossed_etching'),

)

COLOR_COUNT_OPTION_CHOICES = (

('1', '1'),
('2', '2'),
('multi_color', 'multi_color'),

)

COLOR_OPTION_CHOICES = (

('black', 'black'),
('blue', 'blue'),
('red', 'red'),
('green', 'green'),
('yellow', 'yellow'),

)

FONT_HEIGHT_OPTION_CHOICES = (

('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6'),
('7', '7'),
('above_8', 'above_8'),
('combination_of_1to8', 'combination_of_1to8'),

)

THICKNESS_OPTION_CHOICES = (

('0.1' ,'0.1'),
('0.2' ,'0.2'),
('0.3' ,'0.3'),
('0.4' ,'0.4'),
('0.5' ,'0.5'),
('0.6' ,'0.6'),
('0.7' ,'0.7'),
('0.8' ,'0.8'),
('0.9' ,'0.9'),
('1.0' ,'1.0'),
('1.2' ,'1.2'),
('1.5' ,'1.5'),
('2' ,'2'),
('2.5' ,'2.5'),
('3.0' ,'3.0'),

)




class order_child(models.Model):

    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name = "fdthfh")
    item_code = models.TextField()
    material = models.CharField(max_length=50, choices=MATERIAL_OPTION_CHOICES)
    process = models.CharField(max_length=50, choices=PROCESS_OPTION_CHOICES)
    text_matter = models.CharField(max_length=50, choices=TEXT_MATTER_OPTION_CHOICES)
    etching = models.CharField(max_length=50, choices=ETCHING_OPTION_CHOICES)
    color_count = models.CharField(max_length=50, choices=COLOR_COUNT_OPTION_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_OPTION_CHOICES)
    font_height = models.CharField(max_length=50, choices=FONT_HEIGHT_OPTION_CHOICES)
    thickness = models.CharField(max_length=50, choices=THICKNESS_OPTION_CHOICES)
    total_sq_inch = models.FloatField()
    quantity = models.FloatField()
    rate_per_unit = models.FloatField()
    basic_amount = models.FloatField()







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

