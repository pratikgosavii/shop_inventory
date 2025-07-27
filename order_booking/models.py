from django.db import models

# Create your models here.



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
    

    