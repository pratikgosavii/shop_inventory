from django.db import models

# Create your models here.

from transactions.models import *

class order_booking(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('active', 'Active'),
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('hold', 'Hold'),
        ('completed', 'Completed'),
    ]

    ORDER_TYPE_CHOICES = [
        ('new', 'New'),
        ('repeated', 'Repeated'),
    ]

    DELIVERY_TYPE_CHOICES = [
        ('urgent', 'Urgent'),
        ('po_date', 'On PO Date'),
    ]
     
    customer = models.ForeignKey(customer , on_delete=models.CASCADE, related_name='order_customer')
    order_id = models.CharField(unique=True, max_length=50)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', null=True, blank=True)
    total_sqinch = models.IntegerField(null=True, blank=True)

    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES, null=True, blank=True)

    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)

    design_completion_expected_date = models.DateField(null=True, blank=True)
    design_completion_date = models.DateField(auto_now=False, null=True, blank=True)
    expected_film_delivery_date = models.DateField(null=True, blank=True)

    date = models.DateField(auto_now=True)  

    is_drawing_avaiable = models.BooleanField(default=False)
    is_flim_avaiable = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Auto set is_drawing_avaiable if order_type is new
        if self.order_type == "new":
            self.is_drawing_avaiable = True
        else:
            self.is_drawing_avaiable = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer.name
    
class order_matarial_production(models.Model):

    order = models.ForeignKey(order_booking, on_delete=models.CASCADE, related_name = "order_production_n")
    item_code = models.ForeignKey(item_code, on_delete=models.CASCADE, related_name = "order_prod_item_code", null = True, blank = True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    thickness = models.ForeignKey(thickness, on_delete=models.CASCADE)
    grade = models.ForeignKey(grade, on_delete=models.CASCADE)
    production_quantity = models.IntegerField(null = True, blank = True)
    date_time = models.DateTimeField(auto_now=False, null = True, blank = True)
    size = models.IntegerField(default=0)
    drawings = models.FileField(upload_to='media/project_drawings/', null=True, blank=True)







class production_orders(models.Model):

    HOLD_REASON_CHOICES = [
        ('material_not_available', 'Required material not available'),
        ('unclear_drawing', 'Drawing provided is unclear or incomplete'),
        ('consumables_out_of_stock', 'Consumables currently out of stock'),
        ('power_outage', 'Execution delayed due to power outage'),
        ('manpower_shortage', 'Insufficient manpower to proceed'),
        ('other', 'Other'),
    ]

     

    order = models.ForeignKey(order_booking, on_delete=models.CASCADE, related_name="order_production", blank=True, null=True)
    priority = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    stage = models.CharField(
        max_length=50,
        choices=[
            ('hold', 'Hold'),
            ('not_started', 'Not Started'),
            ('in_progress', 'In Progress'),
            ('cutting', 'Cutting'),
            ('welding', 'Welding'),
            ('assembly', 'Assembly'),
            ('completed', 'Completed'),
            ('painting', 'Painting'),
        ],
        default='not_started'
    )

    hold_reason = models.CharField(max_length=40, choices=HOLD_REASON_CHOICES, null=True, blank=True)
    assigned_employees = models.ManyToManyField("store.cutter", blank=True, related_name="production_orders")
    start_date = models.DateField(null=True, blank=True)
    expected_end_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)

    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Production for {self.order.order_id} ({self.get_stage_display()})"

    