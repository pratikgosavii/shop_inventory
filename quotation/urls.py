from django.urls import path

from .views import *
from store import views

urlpatterns = [

   

   
    path('add-sales-customer/', add_sales_customer, name='add_sales_customer'),
    path('add-sales-customer-json/', add_sales_customer_json, name='add_sales_customer_json'),
    path('customer_details/<int:customer_id>', get_customer_details, name='get_customer_details'),
    path('update-sales-customer/<sales_customer_id>', update_sales_customer, name='update_sales_customer'),
    path('delete-sales-customer/<sales_customer_id>', delete_sales_customer, name='delete_sales_customer'),
    path('list-sales-customer/', list_sales_customer, name='list_sales_customer'),


    path('gettoken/', gettoken, name='add_order'),
    path('send_qutation_notification/<order_id>', send_qutation_notification, name='send_qutation_notification'),
    path('add-order/', add_order, name='add_order'),
    path('update-order/<order_id>', update_order, name='update_order'),
    path('delete-order/<order_id>', delete_order, name='delete_order'),
    path('list-order/', list_order, name='list_order'),
    path('print-order/<order_id>', print_order, name='print_order'),
    path('approve-order/<order_id>', approve_order, name='approve_order'),

    
    path('report-sales/', sales_report, name='sales_report'),
    path('download-report-sales/', download_sales_report, name='download_sales_report'),


    path('update_psi/', update_psi, name='update_psi'),


]
