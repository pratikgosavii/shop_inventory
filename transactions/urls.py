from django.urls import path

from .views import *
from store import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [




    path('fix-stock/', demo, name='demo'),

    path('add-request_matrial/', add_request_material, name='add_request_material'),
    path('update-request_material/<request_material_id>', update_request_material, name='update_request_material'),
    path('list-request_material/', list_request_material, name='list_request_material'),
    
    # path('add-product/', add_product, name='add_product'),
    path('update-product/', update_product, name='update_product'),
    
    path('add-project/', add_project, name='add_project'),
    path('update-project/<project_id>', update_project, name='update_project'),
    path('get-sheet-details/', get_sheet_details, name='get_sheet_details'),
    path('list-project/', list_project, name='list_project'),
    path('report-project/', project_report, name='project_report'),
    path('download-report-project/', download_project_report, name='download_project_report'),
    path('close-project/<project_id>', close_project, name='close_project'),
    path('delete-project/<project_id>', delete_project, name='delete_project'),

    path('assign-matarial-qr/<project_id>', assign_matarial_qr, name='assign_matarial_qr'),
    path('delete-matarial-qr/<assign_material_qr_id>', delete_assign_material, name='delete_assign_material'),
    
    path('show-qr', show_scanner_assign_matarial_qr, name='show_scanner_assign_matarial_qr'),
    path('update-assign-matarial-qr/<product_qr_id>', update_assign_matarial_qr, name='update_assign_matarial_qr'),
    path('add_production/<project_id>', add_production, name='add_production'),
    path('delete_production/<project_id>/<production_id>', delete_production_entry, name='delete_production_entry'),
    
    # path('update-project/<project_id>', update_project, name='update_project'),
    # path('list-project/', list_project, name='list_project'),


    path('generate-product-qr/', generate_product_qr, name='generate_product_qr'),
    path('list-generated-product-qr/', list_generated_product_qr, name='list_generated_product_qr'),
    path('print-single-qr/<product_qr_id>', print_single_qr, name='print_single_qr'),
    
    
    path('scanner-page', scanner_page, name='scanner_page'),
    path('assign-values-to-qr/<product_qr_id>', assign_values_to_qr, name='assign_values_to_qr'),
    path('assign-values-to-qr-page', assign_values_to_qr_page, name='assign_values_to_qr_page'),


    path('list-stock/', list_stock, name='list_stock'),
    path('list-left-over-stock/', list_left_over_stock, name='list_left_over_stock'),
    path('list-dead-stock/', list_dead_stock, name='list_dead_stock'),

    path('send-whatsapp-message/', send_whatsapp_message, name='send_whatsapp_message'),

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)