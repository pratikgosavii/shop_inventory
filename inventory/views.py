from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import *


from store.models import *


@login_required(login_url='login')
def dashboard(request):


    godown_data = 4
    godiwn_count = 4
    stock_count = 232

    context = {
        'godown' : godiwn_count,
        'godown_data' : godown_data,
        'stock' : stock_count
    }
    
    return render(request, 'dashboard.html', context)
