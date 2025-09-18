from django.urls import path

from .views import *
from store import views

urlpatterns = [

   

   
   
    path('add-order-booking/', add_order_booking, name='add_order_booking'),
    path('update-order-booking/<order_id>', update_order_booking, name='update_order_booking'),
    path('update-production_order/<production_order_id>', update_production_order, name='update_production_order'),
    path('delete-order-booking/<order_id>', delete_order_booking, name='delete_order_booking'),
    path('list-order-booking/', list_order_booking, name='list_order_booking'),
    
    path('delete-order-production/<production_id>', delete_order_production, name='delete_order_production'),
    path('delete_order_sheet_requiremnt/<order_sheet_id>', delete_order_sheet_requiremnt, name='delete_order_sheet_requiremnt'),

    path('update-order-booking-designer/<order_id>', update_order_booking_designer, name='update_order_booking_designer'),
    
    path('move_to_production/<order_id>', move_to_production, name='move_to_production'),
    path('move_to_planning/<order_id>', move_to_planning, name='move_to_planning'),
    path('mark_as_completed/<production_id>', mark_as_completed, name='mark_as_completed'),
    path('mark_as_hold/<production_id>', mark_as_hold, name='mark_as_hold'),
    path('active_production_order/<production_id>', active_production_order, name='active_production_order'),
    path('production-list/', production_list, name='production_list'),
    
    path("update-priority/", update_priority, name="update_priority"),
    
    path("orders-today-report/", order_today_report, name="order_today_report"),

    

]
