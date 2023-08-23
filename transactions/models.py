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
    employee = models.ForeignKey(employee , on_delete=models.CASCADE, related_name='dsscsdcs')
    DC_date = models.DateField(auto_now_add=False)
    description = models.CharField( max_length=50)
    employee_name = models.CharField( max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

   

class project_material(models.Model):

    quantity = models.IntegerField()
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name = "product_re")
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name = "project_material_re")


    def __str__(self):
        return self.project.employee_name


from store.models import * 

class material_history(models.Model):

    product_qr = models.ForeignKey(product_qr, on_delete=models.CASCADE, related_name = "fdthfh")
    previous_size = models.CharField(max_length=50)
    used_size = models.CharField(max_length=50)
    left_size = models.CharField(max_length=50)


    def __str__(self):
        return self.product_qr.id



class project_matarial_qr(models.Model):
    
    project_material = models.ForeignKey(project_material, on_delete=models.CASCADE, related_name = "project_material_re", null = True, blank = True)
    product_qr =  models.ForeignKey(product_qr, on_delete=models.CASCADE, null = True, blank = True)



class stock(models.Model):

    godown = models.ForeignKey(godown , on_delete=models.CASCADE, related_name='sfwwfddfds')
    quantity = models.BigIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    


