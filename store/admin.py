from django.contrib import admin

from .models import *


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

admin.site.register(category)
admin.site.register(size)
admin.site.register(godown)
admin.site.register(customer)
admin.site.register(product_qr)

