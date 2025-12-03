from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(order_booking)
admin.site.register(order_matarial_production)
admin.site.register(production_orders)
admin.site.register(order_matarial_production_drawing)