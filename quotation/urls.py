from django.urls import path

from .views import *
from store import views

urlpatterns = [

   

   
    path('quotation-dashboard/', quotation_dashboard, name='quotation_dashboard'),

    path('add-sales-customer/', add_sales_customer, name='add_sales_customer'),
    path('add-sales-customer-json/', add_sales_customer_json, name='add_sales_customer_json'),
    path('customer_details/<int:customer_id>', get_customer_details, name='get_customer_details'),
    path('update-sales-customer/<sales_customer_id>', update_sales_customer, name='update_sales_customer'),
    path('delete-sales-customer/<sales_customer_id>', delete_sales_customer, name='delete_sales_customer'),
    path('list-sales-customer/', list_sales_customer, name='list_sales_customer'),

    path('add-color/', add_color, name='add_color'),
    path('update-color/<color_id>', update_color, name='update_color'),
    path('delete-color/<color_id>', delete_color, name='delete_color'),
    path('list-color/', list_color, name='list_color'),

    path('add-etching/', add_etching, name='add_etching'),
    path('update-etching/<etching_id>', update_etching, name='update_etching'),
    path('delete-etching/<etching_id>', delete_etching, name='delete_etching'),
    path('list-etching/', list_etching, name='list_etching'),

    path('add-text-matter/', add_text_matter, name='add_text_matter'),
    path('update-text-matter/<text_matter_id>', update_text_matter, name='update_text_matter'),
    path('delete-text-matter/<text_matter_id>', delete_text_matter, name='delete_text_matter'),
    path('list-text-matter/', list_text_matter, name='list_text_matter'),

    path('add-process/', add_process, name='add_process'),
    path('update-process/<process_id>', update_process, name='update_process'),
    path('delete-process/<process_id>', delete_process, name='delete_process'),
    path('list-process/', list_process, name='list_process'),


    path('gettoken/', gettoken, name='add_order'),
    path('send_qutation_notification/<order_id>', send_qutation_notification, name='send_qutation_notification'),
    path('add-order/', add_order, name='add_order'),
    path('update-order/<order_id>', update_order, name='update_order'),
    path('delete-order/<order_id>', delete_order, name='delete_order'),
    path('list-order/', list_order, name='list_order'),
    path('print-order/<order_id>', print_order, name='print_order'),

    path('approve-order/<order_id>', approve_order, name='approve_order'),
    path('convert-order/<order_id>', convert_order, name='convert_order'),
    path('unconvert-order/<order_id>', unconvert_order, name='unconvert_order'),

    
    path('report-sales/', sales_report, name='sales_report'),
    path('download-report-sales/', download_sales_report, name='download_sales_report'),


    path('get-psi/', get_psi, name='get_psi'),
    path('update-psi/', update_psi, name='update_psi'),


]
