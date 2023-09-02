from django.urls import path

from .views import *
from store import views

urlpatterns = [

    path('get-company_goods-ajax/', get_company_goods_ajax, name="get_company_goods_ajax"),
    path('get-goods_company-ajax/', get_goods_company_ajax, name="get_goods_company_ajax"),
    path('get-agent_company-ajax/', get_agent_company_ajax, name="get_agent_company_ajax"),

    path('get-category_ajax-ajax/', get_category_ajax, name="get_category_ajax"),

    path('add-godown/', add_godown, name='add_godown'),
    path('update-godown/<godown_id>', update_godown, name='update_godown'),
    path('delete-godown/<godown_id>', delete_godown, name='delete_godown'),
    path('list-godown/', list_godown, name='list_godown'),
    

    path('add-item_code/', add_item_code, name='add_item_code'),
    path('update-item_code/<item_code_id>', update_item_code, name='update_item_code'),
    path('delete-item_code/<item_code_id>', delete_item_code, name='delete_item_code'),
    path('list-item_code/', list_item_code, name='list_item_code'),
    
    path('add-customer/', add_customer, name='add_customer'),
    path('update-customer/<customer_id>', update_customer, name='update_customer'),
    path('delete-customer/<customer_id>', delete_customer, name='delete_customer'),
    path('list-customer/', list_customer, name='list_customer'),
    
    path('add-employee/', add_employee, name='add_employee'),
    path('update-employee/<employee_id>', update_employee, name='update_employee'),
    path('delete-employee/<employee_id>', delete_employee, name='delete_employee'),
    path('list-employee/', list_employee, name='list_employee'),
    
    path('add-cutter/', add_cutter, name='add_cutter'),
    path('update-cutter/<cutter_id>', update_cutter, name='update_cutter'),
    path('delete-cutter/<cutter_id>', delete_cutter, name='delete_cutter'),
    path('list-cutter/', list_cutter, name='list_cutter'),

    path('add-dealer/', add_dealer, name='add_dealer'),
    path('update-dealer/<dealer_id>', update_dealer, name='update_dealer'),
    path('delete-dealer/<dealer_id>', delete_dealer, name='delete_dealer'),
    path('list-dealer/', list_dealer, name='list_dealer'),

    path('add-category/', add_category, name='add_category'),
    path('update-category/<category_id>', update_category, name='update_category'),
    path('delete-category/<category_id>', delete_category, name='delete_category'),
    path('list-category/', list_category, name='list_category'),

    
    path('add-grade/', add_grade, name='add_grade'),
    path('update-grade/<grade_id>', update_grade, name='update_grade'),
    path('delete-grade/<grade_id>', delete_grade, name='delete_grade'),
    path('list-grade/', list_grade, name='list_grade'),
    
    path('add-thickness/', add_thickness, name='add_thickness'),
    path('update-thickness/<thickness_id>', update_thickness, name='update_thickness'),
    path('delete-thickness/<thickness_id>', delete_thickness, name='delete_thickness'),
    path('list-thickness/', list_thickness, name='list_thickness'),
    
    path('add-size/', add_size, name='add_size'),
    path('update-size/<company_goods_id>', update_size, name='update_size'),
    path('delete-size/<company_goods_id>', delete_size, name='delete_size'),
    path('list-size/', list_size, name='list_size'),

    #delete urls 

    path('list-godown-delete/', list_godown_delete, name='list_company_delete'),
    path('list-company-goods-delete/', list_company_goods_delete, name='list_company_goods_delete'),
    path('list-goods-company-delete/', list_goods_company_delete, name='list_goods_company_delete'),
    path('list-agent-delete/', list_agent_delete, name='list_agent_delete'),
    path('list-transport-delete/', list_transport_delete, name='list_transport_delete'),






    # 
    # 
    # 
    # 
    # 

]
