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
