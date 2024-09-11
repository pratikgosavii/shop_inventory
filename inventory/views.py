from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import *


from store.models import *
from django.db.models import Sum


@login_required(login_url='login')
def dashboard(request):


    godown_data = 4
    godiwn_count = 4

    stock_count = stock.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']


    context = {
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : stock_count
    }
    
    return render(request, 'dashboard.html', context)





@login_required(login_url='login')
def dashboard_working_order(request):


    data = project_working_order.objects.filter(status = "active")

    godown_data = 4
    godiwn_count = 4

    stock_count = stock.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']


    context = {
        'data' : data,
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : stock_count
    }

    
    return render(request, 'working_order_dashboard.html', context)



from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




@csrf_exempt  # If you're using CSRF protection, don't forget to handle the token
def update_priority(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('order'))
        for item in data:
            data = project_working_order.objects.get(id=item['id'])
            data.priority = item['priority']
            data.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
