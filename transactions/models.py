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

class order_booking(models.Model):

    customer = models.ForeignKey(customer , on_delete=models.CASCADE, related_name='hfgfsdfhjgjvhj')
    employee_name = models.ForeignKey(employee , on_delete=models.CASCADE, null=True, blank=True, related_name='dfdfdfdfsdds')
    DC_date = models.DateField(auto_now_add=False)
    description = models.CharField( max_length=50)
    order_id = models.CharField(unique=True, max_length=50)
    rra_invoice_no = models.CharField(null=True, blank=True, max_length=100)
    completed = models.BooleanField(default=False)
    # design_file = models.FileField(upload_to='media/project_design/')
    # own_design_file = models.FileField(upload_to='media/project_design/', blank=True)
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('hold', 'Hold'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', null=True, blank=True)


    def __str__(self):
        return self.description
    

class project(models.Model):

    customer = models.ForeignKey(customer , on_delete=models.CASCADE, related_name='hfghjgjvhj')
    employee_name = models.ForeignKey(employee , on_delete=models.CASCADE, null=True, blank=True, related_name='dfsdds')
    DC_date = models.DateField(auto_now_add=False)
    description = models.CharField( max_length=50)
    order_id = models.CharField(unique=True, max_length=50)
    rra_invoice_no = models.CharField(null=True, blank=True, max_length=100)
    completed = models.BooleanField(default=False)
    # design_file = models.FileField(upload_to='media/project_design/')
    # own_design_file = models.FileField(upload_to='media/project_design/', blank=True)
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('hold', 'Hold'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', null=True, blank=True)


    def __str__(self):
        return self.description
    



STATUS_CHOICES = [
        ('active', 'Active'),
        ('hold', 'Hold'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]


class project_working_order(models.Model):

    project = models.ForeignKey(project , on_delete=models.CASCADE, related_name='hfghjgjvhj')
    priority = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
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
    length = models.IntegerField()
    width = models.IntegerField()
    

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
    date_time = models.DateTimeField(auto_now=False, null = True, blank = True)
    barcode_count = models.BigIntegerField(default = 0, null = True, blank = True)
    main_label_count = models.BigIntegerField(default = 0, null = True, blank = True)
    invoice_no = models.CharField(null = True, blank=True, max_length=50)



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

    



INDUSTRY_OPTION_CHOICES = (
    ('automotive', 'automotive'),
    ('auto_ancillary', 'auto ancillary'),
    ('sugar', 'sugar'),
    ('domestic_appliance', 'domestic appliance'),
    ('process_equipmen', 'process equipmen'),
    ('petro_chemica', 'petro chemica'),
    ('food_equipmen', 'food equipmen'),
    ('medical_device_equipement', 'medical device & equipement'),
    ('defence', 'defence'),
    ('aviation_aero_space', 'aviation & aero space'),
    ('elevator', 'elevator'),
    ('electricals', 'electricals'),
    ('electronics', 'electronics'),
    ('filteration', 'filteration'),
    )


PRODUCT_OPTION_CHOICES = (
    ('nameplate', 'nameplate'),
    ('front_pannel', 'front pannel'),
    ('nameplate_with_qr_code', 'nameplate with qr code'),
    ('project_based_cable_tags', 'project based cable tags'),
    ('schematic_drg', 'schematic drg'),
    ('thin_shim_and_spacer', 'thin shim & spacer'),
    ('proto_type_stator_and_rotar_lamination', 'proto type stator & rotar lamination'),
    ('regular_thin_mesh', 'regular thin mesh'),
    ('customized_mesh', 'customized mesh'),
    ('encoder_disc', 'encoder disc'),
    ('aperture_and_pin_holes', 'aperture & pin holes'),
    ('texturing', 'texturing'),
    ('speaker_grill', 'speaker grill'),
    ('contact_connector_and_terminals', 'contact , connector & terminals'),
    ('valve_and_compressor_plate', 'valve & compressor plate'),
    ('diaphragm', 'diaphragm'),
    ('emi_rfi_shielding', 'emi / rfi shielding'),
    ('filteration', 'filteration'),
    ('battery_contact', 'battery contact'),
    ('antenna_tele_communication', 'antenna tele communication'),
    ('bipolar_plate_pem', 'bipolar plate pem'),
    ('flat_spring_u_spring_v_spring', 'flat spring, u spring, v spring'),
    ('metal_business_card_with_nfc_chip', 'metal business card with nfc chip'),
    ('metal_business_card_without_chip', 'metal business card without chip'),
    ('book_mark_and_product_model', 'book mark & product model'),
    ('designer_stainless_steel_sheet', 'designer stainless steel sheet'),
    ('designer_stainless_steel_sheet_with_elevator_cabinet', 'designer stainless steel sheet with elevator cabinet'),
    ('designer_stainless_steel_sheet_with_elevator_cabinet_roof_and_bottom', 'designer stainless steel sheet with elevator cabinet, roof & bottom'),
)

FILE_FORMAT_CHOICES = (
    ('cdr', 'CDR'),
    ('dxf', 'DXF'),
    ('ai', 'A.I'),
    ('pdf', 'PDF'),
    ('excel', 'Excel'),
)

INCOTERM_CHOICES = (
    ('ex-works', 'Ex-Works'),
    ('f.o.b.', 'F.O.B.'),
    ('c_and_f', 'C & F'),
    ('cif', 'CIF'),
    ('warehouse_to_warehouse', 'Warehouse to Warehouse'),
)

TRANSPORT_CHOICES = (
    ('road', 'Road'),
    ('rail', 'Rail'),
    ('air', 'Air'),
    ('courier', 'Courier'),
    ('porter', 'Porter'),
    ('personal_pick_up', 'Personal Pick Up'),
)

PAYMENT_CHOICES = (
    ('advance', 'advance'),
    ('against_delivery', 'against_delivery'),
    ('proforma_invoice ', 'proforma_invoice'),
    ('credit_in_day ', 'credit_in_day'),
)

REJECTION_ACCEPTANCE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)



SUDDENT_RISE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

SUDDENT_RISE_PERCENT_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
)


PACKAGING_CHOICES = (
    ('paper', 'Paper'),
    ('plastic_bags', 'Plastic Bags'),
    ('corrugated_box', 'Corrugated Box'),
    ('wooden_box', 'Wooden Box'),
)

REFERENCE_FROM_OPTION_CHOICES = (
    ('Direct_Contact', 'Direct_Contact'),
    ('Webiste', 'Webiste'),
    ('Mailer', 'Mailer'),
)



PACKAGING_CHARGES_CHOICES = (
        (0, '0'),
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500'),
        (600, '600'),
        (700, '700'),
        (800, '800'),
        (900, '900'),
        (1000, '1000'),
        (1100, '1100'),
        (1200, '1200'),
        (1300, '1300'),
        (1400, '1400'),
        (1500, '1500'),
        (1600, '1600'),
        (1700, '1700'),
        (1800, '1800'),
        (1900, '1900'),
        (2000, '2000'),
        (2100, '2100'),
        (2200, '2200'),
        (2300, '2300'),
        (2400, '2400'),
        (2500, '2500'),
        (2600, '2600'),
        (2700, '2700'),
        (2800, '2800'),
        (2900, '2900'),
        (3000, '3000'),
        (3100, '3100'),
        (3200, '3200'),
        (3300, '3300'),
        (3400, '3400'),
        (3500, '3500'),
        (3600, '3600'),
        (3700, '3700'),
        (3800, '3800'),
        (3900, '3900'),
        (4000, '4000'),
        (4100, '4100'),
        (4200, '4200'),
        (4300, '4300'),
        (4400, '4400'),
        (4500, '4500'),
        (4600, '4600'),
        (4700, '4700'),
        (4800, '4800'),
        (4900, '4900'),
        (5000, '5000'),
    )



		



# models.py
from django.db import models
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





class project_outward_main_label(models.Model):

    project_matarial_production = models.ForeignKey(project_matarial_production, null = True, blank = True, on_delete=models.CASCADE, related_name='outward_item_code_main_label')
    quantity = models.IntegerField()
    date_time = models.DateTimeField(auto_now=False, null = True, blank = True)


class project_outward(models.Model):

    project_matarial_production = models.ForeignKey(project_matarial_production , on_delete=models.CASCADE, related_name='outward_item_code_barcode')
    quantity = models.IntegerField()
    date_time = models.DateTimeField(auto_now=False, null = True, blank = True)
    main_label = models.ForeignKey(project_outward_main_label, null = True, blank = True, on_delete=models.CASCADE, related_name='main_label_re')


class inward_item_code(models.Model):

    item_code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, null = True, blank = True)
    

    def __str__(self):
        return self.item_code
    

    

    
class project_inward(models.Model):

    inward_item_code = models.ForeignKey(inward_item_code, on_delete=models.CASCADE)
    inward_supplier = models.ForeignKey(inward_supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False)

