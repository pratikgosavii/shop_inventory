from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(order_child)
admin.site.register(order)
admin.site.register(sales_customer)
admin.site.register(etching)
admin.site.register(color)
admin.site.register(text)
admin.site.register(PSI)