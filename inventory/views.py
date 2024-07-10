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




