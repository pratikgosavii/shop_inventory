from django.urls import path

from .views import *
from store import views

urlpatterns = [

   

   
   
    path('add-order/', add_order, name='add_order'),
 
  

]
