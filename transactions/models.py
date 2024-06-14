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
    ('yes', 'Yes'),
    ('no', 'No'),
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



		     
class sales_customer(models.Model):

    
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    client_gst = models.CharField(max_length=120, unique=False)
    
    
    def __str__(self):
        return self.name
    

from users.models import User
		     
class order(models.Model):
    
    customer = models.ForeignKey(sales_customer, on_delete=models.CASCADE)
    contance_person_no = models.TextField(null = True, blank = True)
    contact_no = models.TextField(null = True, blank = True)
    email = models.TextField(null = True, blank = True)
    date = models.DateTimeField(null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reference_from = models.CharField(max_length=100, choices=REFERENCE_FROM_OPTION_CHOICES)
    
    industry = models.CharField(max_length=100, choices=INDUSTRY_OPTION_CHOICES)
    product = models.CharField(max_length=100, choices=PRODUCT_OPTION_CHOICES)
    file_format = models.CharField(max_length=100, choices=FILE_FORMAT_CHOICES)
    incoterm = models.CharField(max_length=100, choices=INCOTERM_CHOICES)
    transportation_type = models.CharField(max_length=100, choices=TRANSPORT_CHOICES)
    transportation_cost = models.IntegerField()
    
    payment = models.CharField(max_length=100, choices=PAYMENT_CHOICES)
    advance = models.IntegerField(null = True, blank = True)
    credit_in_days = models.IntegerField(null = True, blank = True)
    
    credit_limit = models.IntegerField()
    rejection_acceptance = models.CharField(max_length=100, choices=REJECTION_ACCEPTANCE)
    
    offer_valid_date = models.DateField()

    sudden_rise = models.CharField(max_length=100, choices=SUDDENT_RISE_CHOICES)
    sudden_rise_percent = models.CharField(max_length=100, choices=SUDDENT_RISE_PERCENT_CHOICES, null = True, blank = True)
    
    packaging  = models.CharField(max_length=100, choices=PACKAGING_CHOICES)
    packaging_charges = models.IntegerField(choices=PACKAGING_CHARGES_CHOICES)

    total_sqinch = models.FloatField()
    final_amount = models.FloatField()
    is_approved = models.BooleanField(default=False)






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

MIN_FONT_HEIGHT_OPTION_CHOICES = (

('1mm', '1mm'),
('600mm', '600mm'),

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

CHARGES_TYPE_OPTION_CHOICES = (

('with_gst' ,'with_gst'),
('with_job_shop' ,'with_job_shop'),

)

FLIM_CHARGES_OPTION_CHOICES = (

('inclusive' ,'inclusive'),
('sqinch' ,'sqinch'),

)

SAMPLE_OPTION_CHOICES = (

('Free_in_case_confirm_Order' ,'Free_in_case_confirm_Order'),
('Extra_Charges_Rs' ,'Extra_Charges_Rs'),

)

CERTIFICATE_OPTION_CHOICES = (

('Free_along_with_invoice' ,'Free_along_with_invoice'),
('No_certification' ,'No_certification'),
('Extra_Charges' ,'Extra_Charges'),

)




class order_child(models.Model):

    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name = "fdthfh")
    item_code = models.TextField()
    material = models.CharField(max_length=50, choices=MATERIAL_OPTION_CHOICES)
    other_material = models.CharField(max_length=50, null = True, blank = True)
    process = models.CharField(max_length=50, choices=PROCESS_OPTION_CHOICES)
    text_matter = models.CharField(max_length=50, choices=TEXT_MATTER_OPTION_CHOICES)
    etching = models.CharField(max_length=50, choices=ETCHING_OPTION_CHOICES)
    color_count = models.CharField(max_length=50, choices=COLOR_COUNT_OPTION_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_OPTION_CHOICES)
    font_height = models.CharField(max_length=50, choices=FONT_HEIGHT_OPTION_CHOICES)
    min_font_height = models.CharField(max_length=50, choices=MIN_FONT_HEIGHT_OPTION_CHOICES)
    thickness = models.CharField(max_length=50, choices=THICKNESS_OPTION_CHOICES)
    length = models.FloatField(null = True, blank = True)
    total_sq_inch = models.FloatField(null = True, blank = True)
    width = models.FloatField(null = True, blank = True)
    quantity = models.FloatField(null = True, blank = True)
    rate_per_unit = models.FloatField(null = True, blank = True)
    basic_amount = models.FloatField(null = True, blank = True)
    charges_type_group = models.CharField(max_length=50, choices=CHARGES_TYPE_OPTION_CHOICES)
    total_with_job_shop = models.FloatField(null = True, blank = True)
    total_with_gst = models.FloatField(null = True, blank = True)
    total_amount_with_charges_type = models.FloatField(null = True, blank = True)
    flim_charges = models.CharField(max_length=50, choices= FLIM_CHARGES_OPTION_CHOICES)
    flim_sqinch = models.CharField(max_length=50,null = True, blank = True)
    flim_charges_total = models.FloatField(null = True, blank = True)
    sample = models.CharField(max_length=50, choices= SAMPLE_OPTION_CHOICES)
    sample_price = models.FloatField(null = True, blank = True)
    certificate_cost = models.CharField(max_length=50, choices= CERTIFICATE_OPTION_CHOICES)
    certificate_price = models.FloatField(null = True, blank = True)
    final_item_total = models.FloatField(null = True, blank = True)









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

