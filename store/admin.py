from django.contrib import admin

from .models import *


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

admin.site.register(category)
admin.site.register(size)
admin.site.register(thickness)
admin.site.register(godown)
admin.site.register(customer)
admin.site.register(product_qr)
admin.site.register(product)
admin.site.register(employee)
admin.site.register(shelf)
admin.site.register(product_qr_shelf)
admin.site.register(item_code)
admin.site.register(SheetCut)

