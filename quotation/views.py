from django.shortcuts import render

# Create your views here.



import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from email import message
from genericpath import samefile
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd
import requests


from store.views import numOfDays
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.urls import reverse
import csv
import mimetypes
from email import message




import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

 
       

# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




@login_required(login_url='login')
def quotation_dashboard(request):

    total_employee = User.objects.filter(is_salesman = True).count()
    total_quotation = order.objects.all().count()

    print(total_employee)
    print(total_quotation)

    context = {
        'total_employee' : total_employee,
        'total_quotation' : total_quotation,
    }

    return render(request, 'quotation_dashboard.html', context)



@login_required(login_url='login')
def add_sales_customer(request):

    if request.method == 'POST':

        forms = sales_customer_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_sales_customer')
        else:
            print(forms.errors)
    
    else:

        forms = sales_customer_Form()

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_sales_customer.html', context)

        

@login_required(login_url='login')
def add_sales_customer_json(request):

    if request.method == 'POST':

        forms = sales_customer_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return JsonResponse({'customer': {'id': forms.instance.id, 'name': forms.instance.name, 'credit_limit': forms.instance.credit_limit}}, status=200)
        else:
            print(forms.errors)
    
    else:

        forms = sales_customer_Form()

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_sales_customer.html', context)



@login_required(login_url='login')
def get_customer_details(request, customer_id):

    try:
        customer_instance = sales_customer.objects.get(id=customer_id)
        customer_data = {
            'credit_limit': customer_instance.credit_limit,
        }
        return JsonResponse({'customer': customer_data}, status=200)
    except sales_customer.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)



@login_required(login_url='login')
def update_sales_customer(request, sales_customer_id):

    if request.method == 'POST':

        instance = sales_customer.objects.get(id=sales_customer_id)

        forms = sales_customer_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_sales_customer')
        else:
            print(forms.errors)
    
    else:

        instance = sales_customer.objects.get(id=sales_customer_id)
        forms = sales_customer_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_sales_customer.html', context)

        

@login_required(login_url='login')
def delete_sales_customer(request, sales_customer_id):

    sales_customer.objects.get(id=sales_customer_id).delete()

    return HttpResponseRedirect(reverse('list_sales_customer'))


        


@login_required(login_url='login')
def list_sales_customer(request):

    data = sales_customer.objects.all()

    context = {
        'data': data
    }

    return render(request, 'quotation/list_sales_customer.html', context)


@login_required(login_url='login')
def add_color(request):

    if request.method == 'POST':

        forms = color_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_color')
        else:
            print(forms.errors)
    
    else:

        forms = color_Form()

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_color.html', context)

        


@login_required(login_url='login')
def update_color(request, color_id):

    if request.method == 'POST':

        instance = color.objects.get(id=color_id)

        forms = color_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_color')
        else:
            print(forms.errors)
    
    else:

        instance = color.objects.get(id=color_id)
        forms = color_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_color.html', context)

        

@login_required(login_url='login')
def delete_color(request, color_id):

    color.objects.get(id=color_id).delete()

    return HttpResponseRedirect(reverse('list_color'))


        


@login_required(login_url='login')
def list_color(request):

    data = color.objects.all()

    context = {
        'data': data
    }

    return render(request, 'quotation/list_color.html', context)


@login_required(login_url='login')
def add_etching(request):

    if request.method == 'POST':

        forms = etching_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_etching')
        else:
            print(forms.errors)
    
    else:

        forms = etching_Form()

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_etching.html', context)

        


@login_required(login_url='login')
def update_etching(request, etching_id):

    if request.method == 'POST':

        instance = etching.objects.get(id=etching_id)

        forms = etching_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_etching')
        else:
            print(forms.errors)
    
    else:

        instance = etching.objects.get(id=etching_id)
        forms = etching_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_etching.html', context)

        

@login_required(login_url='login')
def delete_etching(request, etching_id):

    etching.objects.get(id=etching_id).delete()

    return HttpResponseRedirect(reverse('list_etching'))


        


@login_required(login_url='login')
def list_etching(request):

    data = etching.objects.all()

    context = {
        'data': data
    }

    return render(request, 'quotation/list_etching.html', context)


@login_required(login_url='login')
def add_text_matter(request):

    if request.method == 'POST':

        forms = text_matter_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_text_matter')
        else:
            print(forms.errors)
    
    else:

        forms = text_matter_Form()

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_text_matter.html', context)

        


@login_required(login_url='login')
def update_text_matter(request, text_matter_id):

    if request.method == 'POST':

        instance = text_matter.objects.get(id=text_matter_id)

        forms = text_matter_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_text_matter')
        else:
            print(forms.errors)
    
    else:

        instance = text_matter.objects.get(id=text_matter_id)
        forms = text_matter_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_text_matter.html', context)

        

@login_required(login_url='login')
def delete_text_matter(request, text_matter_id):

    text_matter.objects.get(id=text_matter_id).delete()

    return HttpResponseRedirect(reverse('list_text_matter'))


        


@login_required(login_url='login')
def list_text_matter(request):

    data = text_matter.objects.all()

    context = {
        'data': data
    }

    return render(request, 'quotation/list_text_matter.html', context)



@login_required(login_url='login')
def add_process(request):

    if request.method == 'POST':

        forms = process_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_process')
        else:
            print(forms.errors)
    
    else:

        forms = process_Form()

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_process.html', context)

        


@login_required(login_url='login')
def update_process(request, process_id):

    if request.method == 'POST':

        instance = process.objects.get(id=process_id)

        forms = process_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_process')
        else:
            print(forms.errors)
    
    else:

        instance = process.objects.get(id=process_id)
        forms = process_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'quotation/add_process.html', context)

        

@login_required(login_url='login')
def delete_process(request, process_id):

    process.objects.get(id=process_id).delete()

    return HttpResponseRedirect(reverse('list_process'))


        


@login_required(login_url='login')
def list_process(request):

    data = process.objects.all()

    context = {
        'data': data
    }

    return render(request, 'quotation/list_process.html', context)



def gettoken(request):


    return render(request, 'transactions/gettoken.html')


access_token = "EAALeGznz5UwBO9cCf9mrwEd1vHBgB8neIziWXhS4AKGY02ZCVbfb5bTnSK7TCX6Qo1V0MZCHg7hNHQJYsNIZB17zlXaXFLv4HWJFWHZA0zeK57eZCClKyKxeAROKBh0kWB9PtjGbJeJsDWQSdqIjr20xrOBvk09nfWZCRn4xi5MTuyhco7C3U9P4OZBRbADDzLfKwZDZD"
# recipient_number = ["8237377298"]
recipient_number = ["9765054243", "8767515210", "8237377298"]
template_name = "qutation_added"
language_code = "en"


from django.core.mail import EmailMessage


def send_qutation_notification(request, token, recipient_number, template_name, language_code, parameter_value):


   
    msg = "New Qutation Added Visit \n" + 'https://shopinventory.pythonanywhere.com/transactions/update-order/' + str(parameter_value)
    email = EmailMessage(
            subject='New Quotation Added',
            body=msg,
            from_email='rradailyupdates@gmail.com',
            # to=['pratikgosavi654@gmail.com', 'varad@ravirajanodisers.com', 'ravi@ravirajanodisers.com', 'raj@ravirajanodisers.com'],
            to=['pratikgosavi654@gmail.com'],
        )

   
    # Send the email
    email.send()

def send_salesman_edit_notification(saleman_email, parameter_value):


   
    msg = "Qutation Edited Please Review Visit \n" + 'https://shopinventory.pythonanywhere.com/transactions/update-order/' + str(parameter_value)
    email = EmailMessage(
            subject='New Quotation Added',
            body=msg,
            from_email='rradailyupdates@gmail.com',
            # to=['varad@ravirajanodisers.com', 'ravi@ravirajanodisers.com', 'raj@ravirajanodisers.com'],
            to=['pratikgosavi654@gmail.com', saleman_email],
        )

   
    # Send the email
    email.send()






from datetime import datetime, timedelta


@login_required(login_url='login')
def add_order(request):

    if request.method == 'POST':


        print('-----------')

        orders_data_json = request.POST.get('orders', '[]')
        orders_data = json.loads(orders_data_json)

        updated_request = request.POST.copy()
        updated_request.update({'user': request.user})

        forms_order = order_Form(updated_request)

        if forms_order.is_valid():

            forms_order.save()
            
            for item in orders_data:
               
                item['order'] = forms_order.instance.id
                forms = OrderChildForm(item)
                if forms.is_valid():

                    forms.save()

                    

                else:

                    print(forms.errors)

            send_qutation_notification(request, access_token, recipient_number, template_name, language_code, forms_order.instance.id)

            return JsonResponse({"success": True, "message": "Order submitted successfully!"})
        
        else:
            # Send errors back to the frontend
            print(forms_order.errors)
            return JsonResponse({"success": False, "errors": forms_order.errors})

      
        
        # forms = order_child_Form(request.POST)

        # if forms.is_valid():
        #     forms.save()
        #     return JsonResponse({'status' : 'done', 'instance' : forms.instance.item_code})
        # else:
        #     print(forms.errors)
    
    else:

      
        forms = order_Form()

        color_data = color.objects.all()
        thickness_data = thickness.objects.all()
        etching_data = etching.objects.all()
        text_matter_data = text_matter.objects.all()
        process_data = process.objects.all()

        context = {
            'form': forms,
            'order_no' : '1',
            'date' : datetime.now(),
            'color_data' : color_data,
            'thickness_data' : thickness_data,
            'etching_data' : etching_data,
            'text_matter_data' : text_matter_data,
            'process_data' : process_data,
                              
        }

         # Check if the request is coming from a mobile device
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        is_mobile = 'Mobile' in user_agent

        if is_mobile:
            
            return render(request, 'quotation/add_order_mobile.html', context)

        else:

            return render(request, 'quotation/add_order.html', context)


@csrf_exempt
def update_explanation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        reason_id = data.get("id")
        description = data.get("description")

        try:
            reason = edit_reasons.objects.get(id=reason_id)
            reason.description = description
            reason.save()
            return JsonResponse({"success": True})
        except edit_reasons.DoesNotExist:
            return JsonResponse({"success": False, "error": "Reason not found"})

    return JsonResponse({"success": False, "error": "Invalid request"})




import copy


@login_required(login_url='login')
def update_order(request, order_id):

    instance = order.objects.get(id = order_id)


    if request.method == 'POST':

        print('-----------------------1-------------------')



        orders_data_json = request.POST.get('orders', '[]')
        deletedOrderIdss = request.POST.get('deletedOrderIds')
        explanation = request.POST.get('edit_explanation')
        orders_data = json.loads(orders_data_json)

        if deletedOrderIdss:
            deleted_order_ids = json.loads(deletedOrderIdss)

            for i in deleted_order_ids:


                order_child.objects.get(id = i).delete()

        updated_request = request.POST.copy()

        if not request.user.is_superuser:
            updated_request.update({'user': request.user})
            updated_request.update({'is_approved': True})
        
        else:

            updated_request.update({'user': instance.user})




        forms_order = order_Form(updated_request, instance = instance)

        if forms_order.is_valid():

            forms_order.save()

            print('-----------1-------------')
            instance1 = edit_reasons.objects.create(order=forms_order.instance, description=explanation)
            print(instance1)
            print('------------------------')


            for item in orders_data:


                order_child_instance = order_child.objects.get(id = item['id'])
                item['order'] = forms_order.instance.id
                
                forms = OrderChildForm(item, instance = order_child_instance)
                if forms.is_valid():

                    forms.save()



                else:

                    return JsonResponse({'status' : 'error'})

            send_salesman_edit_notification(instance.user.email, order_id)
        
            return JsonResponse({"success": True, "message": "Form submitted successfully!"})
        

        else:
            # Send form errors back to the frontend

            print(forms_order.errors)
            
            return JsonResponse({"success": False, "errors": forms_order.errors})

      
        
    else:


        instance = order.objects.get(id=order_id)
        forms = order_Form(instance=instance)
        order_child_instance = order_child.objects.filter(order=instance)
        order_child_instance_copy = copy.copy(order_child_instance)
        # Convert date fields to string representations
        instance_dict = model_to_dict(instance)
        order_child_instance_list = [model_to_dict(child) for child in order_child_instance]

        
        color_data = color.objects.all()
        thickness_data = thickness.objects.all()
        etching_data = etching.objects.all()
        text_matter_data = text_matter.objects.all()
        process_data = process.objects.all()

        
        
        context = {
            'form': forms,
            'instance': instance,
            'order_child_instance_dict': json.dumps(order_child_instance_list, cls=DjangoJSONEncoder),
            'instance_json': json.dumps(instance_dict, cls=DjangoJSONEncoder),  # Convert instance to JSON string
            'order_child_instance_copy': order_child_instance_copy,  # Convert instance to JSON string
            'color_data' : color_data,
            'thickness_data' : thickness_data,
            'etching_data' : etching_data,
            'text_matter_data' : text_matter_data,
            'process_data' : process_data,
        }
        return render(request, 'quotation/update_order.html', context)

       




@login_required(login_url='login')
def delete_order(request, order_id):

    order.objects.get(id=order_id).delete()

    return HttpResponseRedirect(reverse('list_order'))


 

@login_required(login_url='login')
def list_order(request):

    if request.user.is_superuser:
        data = order.objects.all()
    else:
        data = order.objects.filter(user = request.user)

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'data': data
    }

    return render(request, 'quotation/list_orders.html', context)

def print_order(request, order_id):

    order_data = order.objects.get(id = order_id)
    order_child_data = order_child.objects.filter(order = order_data)

    print(order_child_data)

    
    context = {
        'order_data': order_data,
        'order_child_data': order_child_data
    }

    return render(request, 'quotation/print_orders.html', context)


def approve_order(request, order_id):

    order_instance = order.objects.get(id = order_id)
    order_instance.is_approved = True
    order_instance.save()

    return redirect('list_order')

def convert_order(request, order_id):

    order_instance = order.objects.get(id = order_id)
    order_instance.is_converted = True
    order_instance.save()

    return redirect('list_order')

def unconvert_order(request, order_id):

    order_instance = order.objects.get(id = order_id)
    order_instance.is_converted = False
    order_instance.save()

    return redirect('list_order')




from .filters import *
from django.db.models import Sum
from django.db.models import Count


@login_required(login_url='login')
def sales_report(request):

    data = order.objects.all()
   


    order_filters = order_filter(request.GET, queryset=data)

    filter_data = order_filters.qs

    final_amount = filter_data.aggregate(Sum('final_amount'))['final_amount__sum']
    total_sqinch = filter_data.aggregate(Sum('total_sqinch'))['total_sqinch__sum']

    context = {
        'data': filter_data,
        'final_amount': final_amount,
        'total_sqinch': total_sqinch,
        'order_filter': order_filters,
       
    }

    return render(request, 'transactions/sales_report.html', context)

def download_sales_report(request):

      
    data = order.objects.all()
   
    order_filters = order_filter(request.GET, queryset=data)

    order_filters_data1 = list(order_filters.qs.values_list('customer__name', 'user__username', 'date', 'total_sqinch', 'final_amount'))
    order_filters_data = list(map(list, order_filters_data1))
    

    vals = []
        
    vals1 = []

    
    vals.append([''])
    vals.append(['SALES REPORT'])
    vals.append([''])
    vals.append([''])
    
    vals1.append("Sr No")
    vals1.append("Customer")
    vals1.append("User")
    vals1.append("Date")
    vals1.append("Total SQinch")
    vals1.append("Final Amount")
    vals.append(vals1)

    counteer = 1

    for i in order_filters_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append(i[1])
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        
        vals.append(vals1)



    name = "Sales_Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name

    
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


        link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    with open(path,  'r', newline="") as f:
        mime_type  = mimetypes.guess_type(link)

        response = HttpResponse(f.read(), content_type=mime_type)
        response['Content-Disposition'] = 'attachment;filename=' + str(link)

        return response



from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from .models import *
from .forms import PSIForm
from urllib.parse import urlencode



def get_psi(request):

    thickness = request.GET.get('thickness')
    etching = request.GET.get('etching')
    color = request.GET.get('color')
    text_matter = request.GET.get('text_matter')
    process = request.GET.get('process')
    sq_inch = int(request.GET.get('sqInch'))

    print(thickness)
    print(etching)
    print(color)
    print(text_matter)
    print(process)
    print(sq_inch)

    # Determine the range field based on sq_inch
    if sq_inch <= 576:
        range_field = 'range_576'
    elif 720 <= sq_inch <= 1728:
        range_field = 'range_720_1728'
    elif 1872 <= sq_inch <= 2880:
        range_field = 'range_1872_2880'
    elif 3024 <= sq_inch <= 4032:
        range_field = 'range_3024_4032'
    elif sq_inch >= 4608:
        range_field = 'range_4608'
    else:
        return JsonResponse({'value': None, 'message': 'No valid range found.'})

    # Query the PSI model
    try:
        psi_entry = PSI.objects.get(
            thickness_id=thickness,
            etching_id=etching,
            color_id=color,
            text_matter_id=text_matter,
            process_id=process,
            category_id=1,
        )
        value = getattr(psi_entry, range_field)
        return JsonResponse({'value': value})
    except PSI.DoesNotExist:
        return JsonResponse({'value': None, 'message': 'No matching entry found.'})

def update_psi(request):
    # Fetch thickness and category data
    thicknesses = thickness.objects.all()
    categories = category.objects.all()
    etchings = etching.objects.all()
    colors = color.objects.all()
    texts = text_matter.objects.all()
    processs = process.objects.all()
    
    if request.method == 'POST':

        thickness_id = request.POST.get('thickness')
        category_id = request.POST.get('category')
        etching_id = request.POST.get('etching')
        color_id = request.POST.get('color')
        text_matter_id = request.POST.get('text_matter')
        process_id = request.POST.get('process')

        print(request.POST)

        thickness_data = get_object_or_404(thickness, id=thickness_id)
        category_data = get_object_or_404(category, id=category_id)
        etching_data = get_object_or_404(etching, id=etching_id)
        color_data = get_object_or_404(color, id=color_id)
        text_matter_data = get_object_or_404(text_matter, id=text_matter_id)
        process_data = get_object_or_404(process, id=process_id)

        try:
            PSI_instance = PSI.objects.get(thickness=thickness_data, category=category_data, etching = etching_data, color = color_data, text_matter = text_matter_data, process = process_data)
            form = PSIForm(request.POST, instance=PSI_instance)

        except PSI.DoesNotExist:
            form = PSIForm(request.POST)

        if form.is_valid():
            form.save()  # Save the form data
            url = reverse('update_psi')  # Get the base URL for the view
            query_params = urlencode({'thickness_id': thickness_id, 'category_id': category_id, 'etching_id' : etching_id, 'color_id' : color_id, 'text_matter_id' : text_matter_id, 'process_id' : process_id})  # Encode parameters
            return redirect(f"{url}?{query_params}")
        else:
            print('Form is not valid')
            print(form.errors)  # Print the form errors for debugging

            context = {
                'form': form,
                'thickness': thickness_data,
                'category': category_data,
                'etching': etching_data,
                'color': color_data,
                'text': text_matter_data,
                'thicknesses': thicknesses,
                'categories': categories,
                'etchings': etchings,
                'colors': colors,
                'texts': texts,
                'processs': processs,
            }

            return render(request, 'quotation/update_psi.html', context)

    else: 

        thickness_id = request.GET.get('thickness_id')
        category_id = request.GET.get('category_id')
        etching_id = request.GET.get('etching_id')
        color_id = request.GET.get('color_id')
        text_matter_id = request.GET.get('text_matter_id')
        process_id = request.GET.get('process_id')

        if thickness_id and category_id and etching_id and color_id and text_matter_id:

            print('-------------------------')


            thickness_data = get_object_or_404(thickness, id=thickness_id)
            category_data = get_object_or_404(category, id=category_id)
            etching_data = get_object_or_404(etching, id=etching_id)
            color_data = get_object_or_404(color, id=color_id)
            text_matter_data = get_object_or_404(text_matter, id=text_matter_id)
            process_data = get_object_or_404(process, id=process_id)

            
            try:
                PSI_instance = PSI.objects.get(thickness=thickness_data, category=category_data, etching = etching_data, color = color_data, text_matter = text_matter_data, process = process_data)
                forms = PSIForm(instance=PSI_instance)  # Render an empty form for GET requests
                print('--------------1---------------')

            except PSI.DoesNotExist:
                print('--------------2---------------')

                forms = PSIForm()  # Render an empty form for GET requests

            # Create the form instance with the submitted data
            
            print(category_data.id)
            print(text_matter_data.id)

            context = {
                'form': forms,
                'thickness': thickness_data,
                'category': category_data,
                'etching': etching_data,
                'color': color_data,
                'text': text_matter_data,
                'process': process_data,
                'thicknesses': thicknesses,
                'categories': categories,
                'etchings': etchings,
                'colors': colors,
                'texts': texts,
                'processs' : processs,
            }

            return render(request, 'quotation/update_psi.html', context)
        
        else:


            context = {
                'thicknesses': thicknesses,
                'categories': categories,
                'etchings': etchings,
                'colors': colors,
                'texts': texts,
                'processs' : processs,

            }

            return render(request, 'quotation/update_psi.html', context)
        



