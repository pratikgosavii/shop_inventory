from django.urls import path

from .views import *
from store import views

urlpatterns = [




    path('fix-stock/', demo, name='demo'),

    path('add-request_matrial/', add_request_material, name='add_request_material'),
    path('update-request_material/<request_material_id>', update_request_material, name='update_request_material'),
    path('list-request_material/', list_request_material, name='list_request_material'),
    
    # path('add-product/', add_product, name='add_product'),
    path('update-product/', update_product, name='update_product'),
    
    path('add-project/', add_project, name='add_project'),
    path('list-project/', list_project, name='list_project'),
    path('close-project/', close_project, name='close_project'),

    path('assign-matarial-qr/<project_id>', assign_matarial_qr, name='assign_matarial_qr'),
    
    # path('update-project/<project_id>', update_project, name='update_project'),
    # path('list-project/', list_project, name='list_project'),


    path('generate-product-qr/', generate_product_qr, name='generate_product_qr'),
    
    path('scanner-page', scanner_page, name='scanner_page'),
    path('assign-values-to-qr', assign_values_to_qr, name='assign_values_to_qr'),


    path('list-stock/', generate_report_stock, name='list_stock'),

    path('report-daily/', generate_report_daily, name='report_daily'),
    path('report-inward/', report_inward, name='report_inward'),
    path('report-outward/', report_outward, name='report_outward'),
    path('report-supply-return/', report_supply_return, name='report_supply_return'),
    path('report-stock/', generate_report_stock, name='generate_report'),

    path('report-main/', generate_report_main, name='generate_report_main'),

    path('download', download, name='download'),

    #delete urls 

    path('delete-dashboard', delete_dashboard, name='delete_dashboard'),
    
    path('list-inward-delete/', list_inward_delete, name='list_inward_delete'),
    path('list-outward-delete/', list_outward_delete, name='list_outward_delete'),
    path('list-return-delete/', list_return_delete, name='list_return_delete'),

    path("download-gate-pass/<outward_id>", ResultList, name="list"),






]