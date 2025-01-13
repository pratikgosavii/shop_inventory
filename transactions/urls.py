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

    path('confirm-outward/<project_id>', confirm_outward, name='confirm_outward'),
    
    path('confirm-small-outward-json/<project_outward_id>', confirm_small_outward_json, name='confirm_small_outward_json'),
    path('confirm-main-outward-json/<project_outward_id>', confirm_main_outward_json, name='confirm_main_outward_json'),

    path('add-project-outward-new/<production_material_id>/<small_label>/<main_label>', add_project_outward_new, name='add_project_outward_new'),
    
    path('generate-small-barcode/<int:id>/', generate_small_barcode, name='generate_small_barcode'),
    path('generate-final-barcode/<int:project_matarial_production_id>/', generate_final_barcode, name='generate_final_barcode'),
    path('generate-all-barcode/<int:project_matarial_production_id>/', generate_all_barcode, name='generate_all_barcode'),
    # path('generate-all-final-barcode/<int:project_matarial_production_id>/', generate_all_final_barcode, name='generate_all_final_barcode'),
    
    path('submit-invoice-json/<project_outward_main_label_id>/<invoiceId>', submit_invoice_json, name='submit_invoice_json'),

    path('scan-barcode/', scan_barcode, name='scan_barcode'),
    path('scan-main-barcode/', scan_main_barcode, name='scan_main_barcode'),

    path('add-inward/', add_inward, name='add_inward'),
    path('inward-itemcode-description/', inward_itemcode_description, name='inward_itemcode_description'),
    path('update-inward/<inward_id>', update_inward, name='update_inward'),
    path('delete-inward/<inward_id>', delete_inward, name='delete_inward'),
    path('list-inward', list_inward, name='list_inward'),
    path('inward-report/', inward_report, name='inward_report'),
    path('inward-report-pdf/', download_inward_report_pdf, name='inward_report_download_pdf'),
    path('inward-report_download/', download_inward_report, name='inward_report_download'),
    
    path('confrim-outward-report/', confrim_outward_report, name='confrim_outward_report'),
    path('outward-report/', outward_report, name='outward_report'),
    path('outward-report-csv/', outward_report_csv, name='outward_report_csv'),
    path('download-outward-report-pdf/', download_outward_report_pdf, name='generate_outward_report_pdf'),
    path('outward-report-pdf-email/', send_outward_report_pdf_email, name='generate_outward_report_pdf_email'),
    path('outward-report-pdf-email-daily/', send_outward_report_pdf_email_daily, name='generate_outward_report_pdf_email_daily'),
    

    path('assign-matarial-qr/<project_id>', assign_matarial_qr, name='assign_matarial_qr'),
    path('delete-matarial-qr/<assign_material_id>/<project_id>', delete_assign_material, name='delete_assign_material'),

    path('list-project/', list_project, name='list_project'),
    path('report-project/', project_report, name='project_report'),
    path('download-report-project/', download_project_report, name='download_project_report'),
    path('report-project/', project_report, name='project_report'),
    path('download-report-project/', download_project_report, name='download_project_report'),

    path('close-project/<project_id>', close_project, name='close_project'),
    path('delete-project/<project_id>', delete_project, name='delete_project'),

   
    
    path('show-qr', show_scanner_assign_matarial_qr, name='show_scanner_assign_matarial_qr'),
    path('update-assign-matarial-qr/<product_qr_id>', update_assign_matarial_qr, name='update_assign_matarial_qr'),
    path('get-cutting-values', get_cutting_values, name='get_cutting_values'),
    path('delete-matarial-history/<history_id>', delete_matarial_history, name='delete_matarial_history'),
    path('add_production/<project_id>', add_production, name='add_production'),
    path('delete_production/<project_id>/<production_id>', delete_production_entry, name='delete_production_entry'),
    
    # path('update-project/<project_id>', update_project, name='update_project'),
    # path('list-project/', list_project, name='list_project'),


    path('generate-product-qr/', generate_product_qr, name='generate_product_qr'),
    path('generate-product-qr-with-values/', generate_product_qr_with_values, name='generate_product_qr_with_values'),
    path('from-to-generate-product-qr/', from_to_generate_product_qr, name='from_to_generate_product_qr'),
    path('list-generated-product-qr/', list_generated_product_qr, name='list_generated_product_qr'),

    path('sheet-report/', sheet_report, name='sheet_report'),
    path('sheet-report-downlaod/', sheet_report_downlaod, name='download_sheet_report'),
    path('sheet-status-report/', sheet_status_report, name='sheet_status_report'),
    
    path('print-single-qr/<product_qr_id>', print_single_qr, name='print_single_qr'),
    path('print-label/<project_id>/<product_qr_id>', print_label, name='print_label'),
    
    
    path('scanner-page', scanner_page, name='scanner_page'),
    path('assign-values-to-qr/<product_qr_id>', assign_values_to_qr, name='assign_values_to_qr'),
    path('assign-values-to-qr-page', assign_values_to_qr_page, name='assign_values_to_qr_page'),

    path('delete-history/<history_id>', delete_history, name='delete_history'),


    path('check-sheet/', check_sheet, name='check_sheet'),

    path('list-stock/', list_stock, name='list_stock'),
    path('list-left-over-stock/', list_left_over_stock, name='list_left_over_stock'),
    path('list-dead-stock/', list_dead_stock, name='list_dead_stock'),

    path('delete-images/', delete_images, name='delete_images'),

    path('list-notifications/', list_notifications, name='list_notifications'),
    path('low_stock_report/<notification_id>', low_stock_report, name='low_stock_report'),



    path('script', script, name='script'),
                                                                                                            



    path('send_low_stock_notification/<message_body>', send_low_stock_notification, name='send_low_stock_notification'),
    path('work_alert_notification/<message_body>', work_alert, name='work_alert'),


    path('downald-data/', downalo_data, name='downalo_data'),

    


    path('download', download, name='download'),
    path('demo', demo, name='demo'),
    
    path('assign-rfid-to-sheet-reception_page/<project_id>', assign_rfid_to_sheet_reception_page, name='assign_rfid_to_sheet_reception_page'), #for assigining rfid to sheet
    path('values-to-assign-rfid-to-sheet/<project_id>/<sheet_id>', values_to_assign_rfid_to_sheet, name='values_to_assign_rfid_to_sheet'), #for assigining rfid to sheet
    # path('demo-api/<project_id>/<sheet_id>/<rfid_value>', send_values_to_assign_rfid_to_sheet, name='send_values_to_assign_rfid_to_sheet'), #for assigining rfid to sheet
    # path('demo-api1', assign_rfid_to_sheet, name='assign_rfid_to_sheet'),
    path('sheet-tracking/<sheet_id>/<rfid_value>', sheet_tracking, name='sheet_tracking'), #for assigining rfid to sheet

    # path('productiom', download, name='download'),



    path('sheet-status-active-demo/<sheet_id>/<rfid_value>/<rfid_reader>', sheet_status_active_demo, name='sheet_status_active'),
    path('sheet-status-active/<sheet_id>', sheet_status_active, name='sheet_status_active'),
    path('sheet-status-deactive/<sheet_id>', sheet_status_deactive, name='sheet_status_deactive'),
    # path('data-api/<rfid_value>/<rfid_reader>', data_api, name='data_api'),




    #delete urls 

    path('delete-dashboard', delete_dashboard, name='delete_dashboard'),
    






] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)