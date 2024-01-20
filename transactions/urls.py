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
    
    path('verify_password/', verify_password, name='verify_password'),
    
    path('add-project/', add_project, name='add_project'),
    path('update-project-accountant/<project_id>', update_project_accountant, name='update_project_accountant'),
    path('add-project-designer/<project_id>', add_project_designer, name='add_project_designer'),
    path('update-project/<project_id>', update_project, name='update_project'),
    path('get-sheet-details/', get_sheet_details, name='get_sheet_details'),
    path('list-project/', list_project, name='list_project'),
    path('report-project/', project_report, name='project_report'),
    path('download-report-project/', download_project_report, name='download_project_report'),
    path('close-project/<project_id>', close_project, name='close_project'),
    path('delete-project/<project_id>', delete_project, name='delete_project'),

    path('assign-matarial-qr/<project_id>', assign_matarial_qr, name='assign_matarial_qr'),
    path('delete-matarial-qr/<assign_material_id>/<project_id>', delete_assign_material, name='delete_assign_material'),
    
    path('show-qr', show_scanner_assign_matarial_qr, name='show_scanner_assign_matarial_qr'),
    path('update-assign-matarial-qr/<product_qr_id>', update_assign_matarial_qr, name='update_assign_matarial_qr'),
    path('delete-matarial-history/<history_id>', delete_matarial_history, name='delete_matarial_history'),
    path('add_production/<project_id>', add_production, name='add_production'),
    path('delete_production/<project_id>/<production_id>', delete_production_entry, name='delete_production_entry'),
    
    # path('update-project/<project_id>', update_project, name='update_project'),
    # path('list-project/', list_project, name='list_project'),


    path('generate-product-qr/', generate_product_qr, name='generate_product_qr'),
    path('generate-product-qr-with-values/', generate_product_qr_with_values, name='generate_product_qr_with_values'),
    path('from-to-generate-product-qr/', from_to_generate_product_qr, name='from_to_generate_product_qr'),
    path('list-generated-product-qr/', list_generated_product_qr, name='list_generated_product_qr'),
    path('print-single-qr/<product_qr_id>', print_single_qr, name='print_single_qr'),
    
    
    path('scanner-page', scanner_page, name='scanner_page'),
    path('assign-values-to-qr/<product_qr_id>', assign_values_to_qr, name='assign_values_to_qr'),
    path('assign-values-to-qr-page', assign_values_to_qr_page, name='assign_values_to_qr_page'),

    path('delete-history/<history_id>', delete_history, name='delete_history'),


    path('list-stock/', list_stock, name='list_stock'),
    path('list-left-over-stock/', list_left_over_stock, name='list_left_over_stock'),
    path('list-dead-stock/', list_dead_stock, name='list_dead_stock'),

    path('delete-images/', delete_images, name='delete_images'),

    path('list-notifications/', list_notifications, name='list_notifications'),
    path('llow_stock_report/<notification_id>', low_stock_report, name='low_stock_report'),

    # path('send-whatsapp-message/', send_whatsapp_message, name='send_whatsapp_message'),



    path('add-order/', add_order, name='add_order'),
    path('update-order/<order_id>', update_order, name='update_order'),
    path('delete-order/<order_id>', delete_order, name='delete_order'),
    path('list-order/', list_order, name='list_order'),
    


    path('download', download, name='download'),
    
    path('demo-api/<rfid_value>/<rfid_reader>', demo_api, name='demo_api'),
    path('demo-api1', demo_api1, name='demo_api1'),

    # path('productiom', download, name='download'),



    path('sheet-status-active-demo/<sheet_id>/<rfid_value>/<rfid_reader>', sheet_status_active_demo, name='sheet_status_active'),
    path('sheet-status-active/<sheet_id>', sheet_status_active, name='sheet_status_active'),
    path('sheet-status-deactive/<sheet_id>', sheet_status_deactive, name='sheet_status_deactive'),
    # path('data-api/<rfid_value>/<rfid_reader>', data_api, name='data_api'),




    #delete urls 

    path('delete-dashboard', delete_dashboard, name='delete_dashboard'),
    
    path('list-inward-delete/', list_inward_delete, name='list_inward_delete'),
    path('list-outward-delete/', list_outward_delete, name='list_outward_delete'),
    path('list-return-delete/', list_return_delete, name='list_return_delete'),







] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)