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
    employee_name = models.ForeignKey(employee , on_delete=models.CASCADE, related_name='dfsdds')
    DC_date = models.DateField(auto_now_add=False)
    description = models.CharField( max_length=50)
    order_id = models.CharField( max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

   
class project_material(models.Model):

    quantity = models.IntegerField()
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name = "product_re")
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name = "project_material_re_1")
    

class project_matarial_qr(models.Model):
    
    project_material = models.ForeignKey(project_material, on_delete=models.CASCADE, related_name = "project_material_re", null = True, blank = True)
    product_qr =  models.ForeignKey(product_qr, on_delete=models.CASCADE, null = True, blank = True)
    cutter =  models.ForeignKey(cutter, on_delete=models.CASCADE, null = True, blank = True)

    
    def __str__(self):
        return self.project_material.product.category.name

class project_matarial_production(models.Model):

    project_matarial_qr = models.ForeignKey(project_matarial_qr, on_delete=models.CASCADE, related_name = "project_matarial_qr_production", null = True, blank = True)
    item_code = models.ForeignKey(item_code, on_delete=models.CASCADE, related_name = "item_code_re_1", null = True, blank = True)
    production_quantity = models.IntegerField(null = True, blank = True)
    


from store.models import * 

class material_history(models.Model):

    product_qr = models.ForeignKey(product_qr, on_delete=models.CASCADE, related_name = "fdthfh")
    previous_size =  models.ForeignKey(size, on_delete=models.CASCADE, related_name = "sdsdsc")
    used_size =  models.ForeignKey(size, on_delete=models.CASCADE, related_name = "fscswdcscdthfh")
    left_size =  models.ForeignKey(size, on_delete=models.CASCADE, related_name = "fdsfcsfcscthfh")




class stock(models.Model):

    quantity = models.BigIntegerField(default = 0, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    

class left_over_stock(models.Model):

    quantity = models.BigIntegerField(default = 0, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

class scratch_stock(models.Model):

    quantity = models.BigIntegerField(default = 0, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    


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

@receiver(post_save, sender=alert)
def send_alert_notification(sender, instance, created, **kwargs):

    print('yes')
    if created:
        print('yes2')

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notification_group',  # You can define a group name
            {
                'type': 'send_notification',
                'entry': instance.message  # Serialize your entry as needed
            }
        )