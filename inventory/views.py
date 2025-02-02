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





@login_required(login_url='login')
def dashboard_working_order(request):


    data = project_working_order.objects.filter(status = "active")

    godown_data = 4
    godiwn_count = 4

    data = product_qr.objects.filter(
        moved_to_scratch=False,
        moved_to_left_over=False,
        product__isnull=False
    ).values(
        'product', 
        'product__category__name', 
        'product__size__mm1', 
        'product__size__mm2', 
        'product__size__name', 
        'product__grade__name', 
        'product__thickness__name'
    ).annotate(total_quantity=Count('id')).order_by('product')

    stock_count = data.aggregate(total_quantity1=Sum('total_quantity'))


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
