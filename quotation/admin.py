from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(order_child)
admin.site.register(order)
admin.site.register(sales_customer)
admin.site.register(etching)
admin.site.register(color)
admin.site.register(text_matter)
admin.site.register(PSI)
admin.site.register(edit_reasons)