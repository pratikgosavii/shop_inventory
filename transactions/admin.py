from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *


admin.site.register(project_material)
admin.site.register(project_matarial_qr)
admin.site.register(stock)
admin.site.register(left_over_stock)
admin.site.register(scratch_stock)

admin.site.register(material_history)
admin.site.register(project)
admin.site.register(project_matarial_production)
admin.site.register(alert)
admin.site.register(project_logs)
admin.site.register(notification_table)
admin.site.register(demo)
admin.site.register(sheets_rifd)

admin.site.register(project_working_order)
admin.site.register(project_outward)
admin.site.register(inward_supplier)
admin.site.register(inward_item_code)
admin.site.register(project_outward_main_label)
