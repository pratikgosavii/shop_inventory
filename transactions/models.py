from django.db import models

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

    customer = models.CharField( max_length=50)
    employee_name = models.ForeignKey(employee , on_delete=models.CASCADE, related_name='dfsdds')
    DC_date = models.DateField(auto_now_add=False)
    description = models.CharField( max_length=50)
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
    is_work_done = models.BooleanField(default=False)
    item_code = models.ForeignKey(item_code, on_delete=models.CASCADE, related_name = "item_code_re_1", null = True, blank = True)
    production_quantity = models.IntegerField(null = True, blank = True)

    
    def __str__(self):
        return self.project_material.product.category.name




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

    


