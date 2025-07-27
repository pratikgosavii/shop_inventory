from django.shortcuts import render

# Create your views here.



def add_order(request):

    return render(request, 'add_order.html')