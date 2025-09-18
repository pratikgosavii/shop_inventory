from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import *


from store.models import *
from django.db.models import Sum
from django.db.models import Count



@login_required(login_url='login')
def dashboard(request):


    godown_data = 4
    godiwn_count = 4


    data = product_qr.objects.filter(
        moved_to_scratch=False,
        moved_to_left_over=False,
        product__isnull=False
    ).count()



    context = {
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : data
    }
    
    return render(request, 'dashboard.html', context)




from order_booking.models import *


@login_required(login_url='login')
def dashboard_order_booking(request):


    data = production_orders.objects.filter(stage = "in_progress").order_by('priority')
    
    data_hold = production_orders.objects.filter(stage = "hold").order_by("start_date")

    godown_data = 4
    godiwn_count = 4


    stock_count = 4


    context = {
        'data' : data,
        'data_hold' : data_hold,
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : stock_count
    }

    
    return render(request, 'dashboard_order_booking.html', context)


@login_required(login_url='login')
def dashboard_working_order(request):


    data = production_orders.objects.filter(stage = "in_progress").order_by('priority')
    
    data_hold = production_orders.objects.filter(stage = "hold").order_by("start_date")

    godown_data = 4
    godiwn_count = 4


    stock_count = 4


    context = {
        'data' : data,
        'data_hold' : data_hold,
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : stock_count
    }

    
    return render(request, 'working_order_dashboard.html', context)


from order_booking.forms import *

@login_required(login_url='login')
def dashboard_executor_order(request):


    data = production_orders.objects.filter(stage = "in_progress").order_by("priority")
    data_hold = production_orders.objects.filter(stage = "hold").order_by("start_date")

    print(data_hold)

    godown_data = 4
    godiwn_count = 4

    forms = production_orders_Form()

    stock_count = 4


    context = {
        'data' : data,
        'data_hold' : data_hold,
        'forms' : forms,
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : stock_count
    }

    
    return render(request, 'executor_working_order_dashboard.html', context)



from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


