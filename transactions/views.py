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

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')




def demo(request):

    
    
    s = stock.objects.all()




    for ab in s:

        a = inward.objects.filter(company__company_name = ab.company.company_name, company_goods__name = ab.company_goods.name, goods_company__goods_company_name = ab.goods_company.goods_company_name)
        b = outward.objects.filter(company__company_name =  ab.company.company_name, company_goods__name = ab.company_goods.name, goods_company__goods_company_name = ab.goods_company.goods_company_name)

        x = 0
        y = 0
        z = 0

        for i in a:
            x = x + i.bags
            
        for i in b:
            y = y + i.bags

        for i in c:
            z = z + i.bags

        

        st = x - y + z


        ab.total_bag = st
        ab.save()




from .filters import *
from django.db.models import Sum

@login_required(login_url='login')
def list_stock(request):

   
    data = stock.objects.filter(quantity__gt =  0).prefetch_related('product__project_material_re')
    total_stock = data.aggregate(total_stock=Sum('quantity'))['total_stock']
    context = {
        'data': data,
        'total_stock' : total_stock,
        
    }

    return render(request, 'transactions/list_stock.html', context)

@login_required(login_url='login')
def list_left_over_stock(request):

   
    data = left_over_stock.objects.prefetch_related('product__project_material_re').filter(quantity__gt=0)
   
    context = {
        'data': data,
        
    }

    return render(request, 'transactions/list_left_over_stock.html', context)

@login_required(login_url='login')
def list_dead_stock(request):

   
    data = scratch_stock.objects.prefetch_related('product__project_material_re').filter(quantity__gt=0)
   
    context = {
        'data': data,
        
    }

    return render(request, 'transactions/list_dead_stock.html', context)

@login_required(login_url='login')
def list_notifications(request):

   
    data = notification_table.objects.all()
    
    context = {
        'data': data,
        
    }

    return render(request, 'transactions/list_notifications.html', context)


@login_required(login_url='login')
def low_stock_report(request, notification_id):

   
    data = notification_table.objects.get(id = notification_id)
    
    data.is_reported = True
    data.save()

    return redirect('list_notifications')



@login_required(login_url='login')
def delete_images(request):

   
    data = product_qr.objects.filter(qr_code__isnull=False)

    for i in data:

        i.qr_code.delete()
   
    context = {
        'data': data,
        
    }

    return redirect('list_generated_product_qr')



from datetime import datetime


def add_order(request):

    if request.method == 'POST':

        orders_data_json = request.POST.get('orders', '[]')
        orders_data = json.loads(orders_data_json)


        print(request.POST)
        forms_order = order_Form(request.POST)

        if forms_order.is_valid():

            forms_order.save()

        else:

            print(forms_order.errors)

      
        for item in orders_data:
            print(item)
            item['order'] = forms_order.instance.id
            forms = OrderChildForm(item)
            if forms.is_valid():

                forms.save()

                return JsonResponse({'status' : 'done', 'instance' : forms.instance.item_code})


            else:

                print(forms.errors)


        # forms = order_child_Form(request.POST)

        # if forms.is_valid():
        #     forms.save()
        #     return JsonResponse({'status' : 'done', 'instance' : forms.instance.item_code})
        # else:
        #     print(forms.errors)
    
    else:

      
        forms = order_Form()

        context = {
            'form': forms,
            'order_no' : '1',
            'date' : datetime.now()
                              
        }

         # Check if the request is coming from a mobile device
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        is_mobile = 'Mobile' in user_agent

        if is_mobile:
            
            return render(request, 'transactions/add_order_mobile.html', context)

        else:

            return render(request, 'transactions/add_order.html', context)

        

from django.forms.models import model_to_dict

import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone


@login_required(login_url='login')
def update_order(request, order_id):

    instance = order.objects.get(id = order_id)

    if request.method == 'POST':

        orders_data_json = request.POST.get('orders', '[]')
        orders_data = json.loads(orders_data_json)



        forms_order = order_Form(request.POST, instance = instance)

        if forms_order.is_valid():

            forms_order.save()

        else:

            print(forms_order.errors)

      
        for item in orders_data:

            order_child_instance = order_child.objects.get(id = item.pk)
            
            print(item)
            forms = OrderChildForm(item)
            if forms.is_valid():

                forms.save()



            else:

                print(forms.errors)
                return JsonResponse({'status' : 'error'})

        
        return JsonResponse({'status' : 'done', 'instance' : forms.instance.item_code})

    else:


        instance = order.objects.get(id=order_id)
        forms = order_Form(instance=instance)
        order_child_instance = order_child.objects.filter(order=instance)

        # Convert date fields to string representations
        instance_dict = model_to_dict(instance)
        order_child_instance_list = [model_to_dict(child) for child in order_child_instance]

        print(order_child_instance_list)

        
        context = {
            'form': forms,
            'order_child_instance_dict': json.dumps(order_child_instance_list, cls=DjangoJSONEncoder),
            'instance_json': json.dumps(instance_dict, cls=DjangoJSONEncoder),  # Convert instance to JSON string
        }
        return render(request, 'transactions/update_order.html', context)

        

@login_required(login_url='login')
def delete_order(request, order_id):

    order.objects.get(id=order_id).delete()

    return HttpResponseRedirect(reverse('list_order'))


        

@login_required(login_url='login')
def list_order(request):

    data = order.objects.all()

    context = {
        'data': data
    }

    return render(request, 'transactions/list_orders.html', context)



import csv



def downalo_data(request):

    projects_data = []
    projects_data.append(['Order ID', 'Customer', 'Sheet No', 'Previous Size', 'Used Size',	'Left Size', 'Updated At', 'Cutter'])

    for proj in project.objects.all():

        projects_data.append([proj.order_id, proj.customer, '', '', '',	'', '', ''])


        for material in project_material.objects.filter(project=proj):

            if material.sheet_no:

                try:
                    product_qr_instances = project_matarial_qr.objects.get(id = material.sheet_no)



                    a = material_history.objects.filter(product_qr = product_qr_instances.id, project = proj)


                    for z in a:
                        projects_data.append(['', '', z.product_qr.id, z.previous_size, z.used_size, z.left_size, z.updated_at, z.cutter])

                except project_matarial_qr.DoesNotExist:
                    
                    pass

    # Convert data to DataFrame
    df = pd.DataFrame(projects_data)

    # Export DataFrame to CSV
    df.to_csv('project_data.csv', index=False)




    


from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings

def send_whatsapp_message(request, category, size, thickness, grade):

    # Your message content
    account_sid = 'AC99a2212d49d4b1349fc702d1227c0e00'
    auth_token = '560bf0fc1c4e1ab09c32ca9bda22226c'
    client = Client(account_sid, auth_token)
    msg = 'Category: ' + str(category) + 'Thickness: ' +  str(thickness) + 'Grade: ' + str(grade) + 'Size :' + str(size) + 'Quantity is less than 5'
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=msg,
    to='whatsapp:+918237377298'
    )

    return True


def sheet_tracking(request, sheet_id, rfid_value):


    sheets_rfid_instance = sheets_rifd.objects.get(sheet_id = sheet_id, status = True)

    sheet_tracking_history.objects.create(project_id = sheets_rfid_instance.project_id, sheet_id = sheets_rfid_instance.sheet_id)
    

    context = {

        'sheet_id' : sheet_id,
        'rfid_value' : rfid_value,

    }

    return JsonResponse(context)


def assign_rfid_to_sheet_reception_page(request, project_id):

    project_instance = project.objects.get(id = project_id)

    forms = project_Form(instance = project_instance)

    data_form = product_Form()

    data = project_material.objects.filter(project = project_instance)


    context = {
        'form': forms,
        'data_form': data_form,
        'data': data,
        'project_id': project_id,
    }
    return render(request, 'transactions/assign_rfid_to_sheet_reception_page.html', context)


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from .models import sheets_rifd
import requests
import time

@csrf_exempt
def values_to_assign_rfid_to_sheet(request, project_id, sheet_id):
    
    node_endpoint = "http://192.168.66.98:80"

    try:
        # Make the request to the NodeMCU server
        response = requests.get(node_endpoint)

        # Print the content of the response
        print('Response content:', response.content)

        # Attempt to parse the response as JSON
        rfid_value = response.json()

        # Print the parsed JSON data
        print('Parsed JSON data:', rfid_value)

        # Serialize the response if needed
        serialized_response = json.dumps({'status': rfid_value})

        # Check if the response contains data
        if rfid_value:
            # Check if a sheet with the same project_id, sheet_id, and rfid_value exists
            check_for_active_sheets = sheets_rifd.objects.filter(project_id=project_id, sheet_id=sheet_id, rfid_value=rfid_value, status=True)
            if not check_for_active_sheets:
                sheets_rifd.objects.create(project_id=project_id, sheet_id=sheet_id, rfid_value=rfid_value)
                return JsonResponse(serialized_response, safe=False)
            else:
                return JsonResponse({'status': 'Already active sheet exists'})
        else:
            return JsonResponse({'status': 'No response data'})
       
    except Exception as e:
        # Handle any exceptions that might occur
        return JsonResponse({'status': 'Error', 'error': str(e)})




# def send_values_to_assign_rfid_to_sheet(request, project_id, sheet_id, rfid_value):

#     instance = sheets_rifd.objects.create(project_id = project_id, sheet_id = sheet_id, rfid_value = rfid_value)

#     context = {

#         'project_id' : instance.project_id,
#         'sheet_id' : instance.sheet_id,
#         'status' : 'done'

#     }

#     return JsonResponse(context)


# def assign_rfid_to_sheet(request):

#     instance = values_for_assignment.objects.last()

#     context = {

#         'project_id' : instance.project_id,
#         'sheet_id' : instance.sheet_id,

#     }

#     return JsonResponse(context)



    


def sheet_status_active(request, sheet_id):

    print('----------------')
    product_qr_instance = product_qr.objects.get(id = sheet_id)
    product_qr_instance.status = True
    product_qr_instance.save()

    print(product_qr_instance)

    return redirect(list_generated_product_qr)




def sheet_status_active_demo(request, sheet_id, rfid_value, rfid_reader):

    #check for if values are not equal to 0 

    context = {

        'sheet_id' : sheet_id,
        'rfid_value' : rfid_value,
        'rfid_reader' : rfid_reader,

    }

    return JsonResponse(context)





def sheet_status_deactive(request, sheet_id):

    
    product_qr_instance = product_qr.objects.get(id = sheet_id)
    product_qr_instance.status = False
    product_qr_instance.save()

    print(product_qr_instance)

    return redirect(list_generated_product_qr)





    

    


@login_required(login_url='login')
def download(request):
    # fill these variables with real values


    if request.method == 'POST':

        fl_path =  request.POST.get('link')



        if os.path.exists(fl_path):

            with open(fl_path, 'r' ) as fh:
                mime_type  = mimetypes.guess_type(fl_path)
                print('--------------------')
                print(mime_type)
                response = HttpResponse(fh.read(), content_type=mime_type)
                response['Content-Disposition'] = 'attachment;filename=' + str(fl_path)

                return response



        else:
            messages.error(request, 'path does not exist')


def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

       return 'abc'

@login_required(login_url='login')
def delete_dashboard(request):

    return render(request, 'delete/dashbaord.html')


# delete view


def list_inward_delete(request):

    data = inward.objects.all()


    context = {
        'data': data,
    }

    return render(request, 'delete/list_inward_delete.html', context)


def list_outward_delete(request):

    data = outward.objects.all()



    context = {
        'data': data,
    }

    return render(request, 'delete/list_outward_delete.html', context)

def list_return_delete(request):

    data = supply_return.objects.all()

    # inward_filter_data = inward_filter()

    print(data)

    context = {
        'data': data,
        # 'filter_inward' : inward_filter_data
    }

    return render(request, 'delete/list_return_delete.html', context)











@login_required(login_url='login')
def add_request_material(request):


    if request.method == 'POST':

        forms = request_material_Form(request.POST)

        if forms.is_valid():
            forms.save()

              
            return JsonResponse({'status' : 'done'}, safe=False)


        else:
                
            error = forms.errors.as_json()
            return JsonResponse({'error' : error}, safe=False)

    else:

        forms = request_material_Form()

        context = {
            'form': forms
        }
        return render(request, 'transactions/add_request_material.html', context)



@login_required(login_url='login')
def update_request_material(request, request_material_id ):


    if request.method == 'POST':

        instance_request_material = request_material.objects.get(id = request_material_id)

        forms = request_material_Form(request.POST, instance=instance_request_material)


        if forms.is_valid():


            forms.save()

            return HttpResponseRedirect(reverse('list_request_material'))

               
         
        else:

            instance = request_material.objects.get(id = request_material_id)
            forms = request_material_Form(instance=instance_request_material)

            context = {
                'form': forms,
            }
            

            return render(request, 'transactions/update_request_material.html', context)


    else:

        instance = request_material.objects.get(id = request_material_id)
        forms = request_material_Form(instance = instance)
       

        context = {
            'form': forms,
        }
        return render(request, 'transactions/update_request_material.html', context)


@login_required(login_url='login')
def delete_request_material(request, request_material_id):

    try:
        con = request_material.objects.filter(id = request_material_id).first()
        
        con.delete()

        return HttpResponseRedirect(reverse('list_inward_delete'))


    except:
        return HttpResponseRedirect(reverse('list_inward_delete'))




@login_required(login_url='login')
def list_request_material(request):

  
    data = request_material.objects.all()

    
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'data': data,
       
    }

    return render(request, 'transactions/list_request_material.html', context)

@login_required(login_url='login')
def list_project(request):

  
    data = project.objects.all().order_by("-id")

    
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'data': data,
        'project_filter': project_filter(),
       
    }

    return render(request, 'transactions/list_projects.html', context)


from django.db.models import Q


@login_required(login_url='login')
def project_report(request):

    code = request.GET.get('item_code')
    customer_id = request.GET.get('customer')
    dc_date_from = request.GET.get('from_DC_date')
    dc_date_to = request.GET.get('to_DC_date')

    print(code)
    print(customer_id)
    print(dc_date_from)
    print(dc_date_to)

    item_code_instance = item_code.objects.get(code = code)

    # Initialize a base queryset
    base_query = project_matarial_production.objects.filter(item_code=item_code_instance)

    if customer_id:
        customer_instance = customer.objects.get(id=customer_id)
        base_query = base_query.filter(project_matarial_qr__project_material__project__customer=customer_instance)

    # Check if dc_date_from and dc_date_to are not None before adding date filters
    if dc_date_from:
        base_query = base_query.filter(project_matarial_qr__project_material__project__DC_date__gte=dc_date_from)

    if dc_date_to:
        base_query = base_query.filter(project_matarial_qr__project_material__project__DC_date__lte=dc_date_to)


    data = base_query.all()
   

    context = {
        'data': data,
        'project_filter': project_filter(),
       
    }

    return render(request, 'transactions/projects_report.html', context)

def download_project_report(request):

    data = project.objects.all()
    project_filters = project_filter(request.GET, queryset=data)
    data = project_filters.qs

    # Create an HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    
    # Set the CSV filename and attachment header
    response['Content-Disposition'] = 'attachment; filename="project_report.csv"'

    # Create a CSV writer and write the header row
    writer = csv.writer(response)
    writer.writerow(['Sr no', 'ITEM CODE', 'QUANTITY' ,'CUSTOMER NAME','DATE'])  # Replace with your actual column names

    # Write the data rows
    for index, item in enumerate(data, start=1):

        for related_obj in item.project_material_re_1.all():

            for project_material_obj in related_obj.project_material_re.all():
                for production_obj in project_material_obj.project_matarial_qr_production.all():
                    
                    writer.writerow([index, production_obj.item_code, production_obj.production_quantity, item.customer, item.DC_date])  # Replace with your actual field names

    return response

import json

@login_required(login_url='login')
def close_project(request, project_id):

    print('here')

    if request.method == 'POST':

        print('here')

        print(request.POST)


        project_instance = project.objects.get(id = project_id)
        project_instance.completed = True

        
        quantity = request.POST.getlist('quantity[]')
        item_code = request.POST.getlist('item_code[]')
        material = request.POST.getlist('materialsId[]')

        print('----------------------')
        print(move_to_scratch)
        print('----------------------')



        


        return JsonResponse({'status' : 'done'})
    
    else:

        project_instance = project.objects.get(id = project_id)

        forms = project_Form(instance = project_instance)

        data_form = product_Form()

        data = project_material.objects.filter(project = project_instance)

        print(data)

        context = {
            'form': forms,
            'data_form': data_form,
            'data': data,
            'project_id': project_id,
        }

        return render(request, 'transactions/close_project.html', context)


def delete_project(request, project_id):

    project_instance = project.objects.get(id = project_id)

    project_instance.delete()

    return redirect('list_project')

import pusher

from store.forms import *

@login_required(login_url='login')
def add_project(request):


    if request.method == 'POST':

        print(request.POST)

        # Deserialize the JSON data into a Python object
        forms = project_Form(request.POST, request.FILES)
        
        order_id = request.POST.get("order_id")
       

        quantity = request.POST.getlist('production_quantity')
        item_code_id = request.POST.getlist('item_code')
        production_id = request.POST.getlist('production_id')

        print(quantity)
        print(item_code_id)
        print(production_id)


        if forms.is_valid():

            project_instance = forms.save()


            for a, b, c in zip(production_id, item_code_id, quantity):

                if a and a!= '0':

                    print('here2')

                    project_material_instnace = project_matarial_production.objects.get(id = a)


                    item_code_instance = item_code.objects.get(id = b)

                    project_material_instnace.item_code = item_code_instance
                    project_material_instnace.production_quantity = c
                    
                    project_material_instnace.save()

                    print('here')

                else:

                    print('here3')

                        
                    item_code_instance = item_code.objects.get(id = b)
                    instance = project_matarial_production.objects.create(item_code = item_code_instance, production_quantity = c, project = project_instance)


            a1212 = alert.objects.create(message = "new project created id" + order_id)
            pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                                      key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                                      secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                                      cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                                      ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

            pusher_client.trigger('alerts', 'new-alert', {'message': a1212.message})

            return redirect('list_project')


        else:
                
            print(forms.errors)
            
            data_form = product_Form()

            context = {
                'form': forms,
                'data_form': data_form,
            }
            return render(request, 'transactions/add_project.html', context)


    else:

        forms = project_Form()

        item_code_data = item_code.objects.all()

        context = {
            'form': forms,
            'item_code_data': item_code_data,
        }
        return render(request, 'transactions/add_project.html', context)

@login_required(login_url='login')
def update_project_accountant(request, project_id):

    project_instance = project.objects.get(id = project_id)

    if request.method == 'POST':

        print(request.POST)

        # Deserialize the JSON data into a Python object
        forms = project_Form(request.POST, instance = project_instance)
        


      
        order_id = request.POST.get("order_id")
       
        quantity = request.POST.getlist('production_quantity')
        item_code_id = request.POST.getlist('item_code')
        production_id = request.POST.getlist('production_id')
        print('-----------------------')
        print(production_id)
        print(quantity)
        print(item_code_id)


        if forms.is_valid():

            print('is valid')

            project_instance = forms.save()


            for a, b, c in zip(production_id, item_code_id, quantity):
                print('----------')
                print(a)
                if a and a != '0':

                    project_material_instnace = project_matarial_production.objects.get(id = a)


                    item_code_instance = item_code.objects.get(id = b)

                    project_material_instnace.item_code = item_code_instance
                    project_material_instnace.production_quantity = c
                    
                    project_material_instnace.save()

                    print('here')

                else:
                        
                    item_code_instance = item_code.objects.get(id = b)
                    instance = project_matarial_production.objects.create(item_code = item_code_instance, production_quantity = c, project = project_instance)

                

            a1212 = alert.objects.create(message = "new project created id" + order_id)
            pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                                      key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                                      secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                                      cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                                      ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

            pusher_client.trigger('alerts', 'new-alert', {'message': a1212.message})

            return redirect('list_project')


        else:
                
            print(forms.errors)
            
            data_form = product_Form()

            context = {
                'form': forms,
                'data_form': data_form,
                'project_id': project_id,
            }
            return render(request, 'transactions/update_project_accountant.html', context)


    else:

        forms = project_Form(instance=project_instance)

        production_data = project_matarial_production.objects.filter(project = project_instance)

        item_code_data = item_code.objects.all()

        context = {
            'form': forms,
            'production_data': production_data,
            'item_code_data': item_code_data,
            'project_id': project_id,
        }
        return render(request, 'transactions/update_project_accountant.html', context)


def add_project_designer(request, project_id):


    project_instance = project.objects.get(id = project_id)

    if request.method == 'POST':


        print(request.POST)

        forms = project_Form(request.POST, instance=project_instance)
        


        sheet_no_id = request.POST.getlist("no_need")
        order_id = request.POST.get("order_id")
        employee_name = request.POST.get("employee_name")

        desginer_name = project_instance.employee_name


        filtered_values = project_material.objects.filter(project = project_instance).values_list('sheet_no', flat=True)

        existing_values = [int(value) for value in filtered_values]

        # Find values that are unique to value_list
        sheet_no_id = [int(value) for value in sheet_no_id]

        unique_values = [value for value in sheet_no_id if value not in existing_values]

        print(existing_values)
        print(sheet_no_id)
        print(unique_values)

        if forms.is_valid():
            

            for field in forms.fields:
                old_value = getattr(project_instance, field)
                new_value = forms.cleaned_data[field]
                
                # Compare the old and new values
                if old_value != new_value:
                    # Create a ProjectLog entry to record the change
                    project_logs.objects.create(
                        project=project_instance,
                        field_name=field,
                        old_value=old_value,
                        new_value=new_value
                    )


          
            project_instance = forms.save()

            if unique_values != ['']:

                print('in')
                for a in unique_values:
                    print('in for')
                    try:

                        project_sheets_logs.objects.create(
                        project=project_instance,
                        description='Designer ' + str(desginer_name) + 'new sheet add sheet no: ' + str(a),
                        )

                        aa = product_qr.objects.get(id = a)
                        
                        print('printing a------------------')
                        print(a)

                        print('printing a------------------')
                        obj, created = product.objects.get_or_create(category_id = aa.product.category.id, size_id = aa.product.size.id, grade_id = aa.product.grade.id, thickness_id = aa.product.thickness.id)
                        product_id = obj

                    except product.DoesNotExist:

                        product_id = created

                    project_material_instance = project_material.objects.create(product = product_id, project = project_instance, quantity = 1, sheet_no = a)

                    aaaas = project_matarial_qr.objects.create(project_material = project_material_instance)
                    print('-----------------')
                    print(aaaas)
                    print('-----------------')

            a1212 = alert.objects.create(message = "new project created id" + order_id)
            pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                                      key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                                      secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                                      cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                                      ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

            pusher_client.trigger('alerts', 'new-alert', {'message': a1212.message})

            return redirect('list_project')

        else:

            print(forms.errors)

            data_form = product_Form()

            project_material_data = project_material.objects.filter(project = project_instance)
           
            production_data = project_matarial_production.objects.filter(project = project_instance)



            context = {
                'form': forms,
                'production_data': production_data,
                'project_material_data': project_material_data,
                'data_form': data_form,
                'project_id': project_id,

            }
            return render(request, 'transactions/add_project_designer.html', context)
    
    else:

        forms = project_Form(instance=project_instance)

        data_form = product_Form()

        production_data = project_matarial_production.objects.filter(project = project_instance)
        
        project_material_data = project_material.objects.filter(project = project_instance)
        # project_material_qr = 

        context = {
            'form': forms,
            'production_data': production_data,
            'project_material_data': project_material_data,
            'data_form': data_form,
            'project_id': project_id,
        }
        return render(request, 'transactions/add_project_designer.html', context)



@login_required(login_url='login')
def update_project(request, project_id):

    project_instance = project.objects.get(id = project_id)

    if request.method == 'POST':

        print(request.POST)

        # Deserialize the JSON data into a Python object
        forms = project_Form(request.POST, instance=project_instance)
        sheet_no_id = request.POST.getlist("sheet_no")
        
        for a in sheet_no_id:
            print('in for')
            try:

                aa = product_qr.objects.get(id = a)
                
                print('printing a------------------')
                print(a)

                print('printing a------------------')
                obj, created = product.objects.get_or_create(category_id = aa.product.category.id, size_id = aa.product.size.id, grade_id = aa.product.grade.id, thickness_id = aa.product.thickness.id)
                product_id = obj

            except product.DoesNotExist:

                product_id = created

            project_material_instance = project_material.objects.create(product = product_id, project = project_instance, quantity = 1, sheet_no = a)

            aaaas = project_matarial_qr.objects.create(project_material = project_material_instance)
            print('-----------------')
            print(aaaas)
            print('-----------------')


       
        print(sheet_no_id)

        if forms.is_valid():

            print('is valid')

            project_instance = forms.save()

            
            return redirect('list_project')


        else:
                
            print(forms.errors)
            

            context = {
                'form': forms,
                'data_form': data_form,
            }
            return render(request, 'transactions/update_project.html', context)


    else:

        forms = project_Form(instance=project_instance)

        data_form = product_Form()
        project_material_data = project_material.objects.filter(project = project_instance)
        material_data = project_matarial_qr.objects.filter(project_material__in = project_material_data)

        context = {
            'form': forms,
            'data_form': data_form,
            'material_data': material_data,
            'project_id': project_id,
        }
        return render(request, 'transactions/update_project.html', context)

@login_required(login_url='login')
def get_sheet_details(request):

    sheet_no = request.POST.get('sheet_no')
    print(sheet_no)

    try:

        instance = product_qr.objects.get(id = sheet_no)
    except product_qr.DoesNotExist:

        return JsonResponse({'status' : 'error', 'msg' : 'Sheet No : ' + sheet_no + ' Does not exsist'})
    
    
    data = {
            'size': instance.product.size.id,
            'grade': instance.product.grade.id,
            'thickness': instance.product.thickness.id,
            'category': instance.product.category.id,
            # Add more fields as needed
        }

    print(data)

    return JsonResponse({"status" : 'done', 'data' : data})



@login_required(login_url='login')
def assign_matarial_qr(request, project_id):

    print('hereeeeeeeeeeeeee')
    print(request.POST)
    print('------------')

    project_instance = project.objects.get(id = project_id)


    if request.method == 'POST':

        

        material = request.POST.getlist('material_id[]')
        scan = request.POST.getlist('scanned_value[]')



        print(material)
        print(scan)

        for i, z in zip(material, scan):

            print('-----------------')

            pro = project_matarial_qr.objects.get(id = i)
            print(pro)
            product_qr_instance = product_qr.objects.get(id = z)
            print(product_qr_instance)

            pro.product_qr = product_qr_instance
            pro.save()
            print('-----------------')


        url = reverse('list_project')

        print(url)

        some_data_to_dump = {
            'status': 'done',
            'url': url,
        }


        return JsonResponse((some_data_to_dump), safe = False) 




       


    else:

        forms = project_Form(instance = project_instance)

        data_form = product_Form()

        data = project_material.objects.filter(project = project_instance)


        context = {
            'form': forms,
            'data_form': data_form,
            'data': data,
            'project_id': project_id,
        }
        return render(request, 'transactions/assign_material_qr.html', context)


def delete_assign_material(request, assign_material_id, project_id):

    project_instance = project.objects.get(id = project_id)
    project_material_instance = project_material.objects.get(id=assign_material_id)
    project_material_qr_instance = project_matarial_qr.objects.get(project_material = project_material_instance, project_material__project = project_instance)
    project_material_qr_instance.delete()

    desginer_name = project_instance.employee_name

    project_sheets_logs.objects.create(
                        project=project_instance,
                        description='Designer ' + str(desginer_name) + 'new sheet add sheet no: ' + str(project_material_instance.sheet_no),
                        )
    
    project_material_instance.delete()

    # Assuming 'project_id' is the correct keyword argument for your 'update_project' view.
    return redirect('add_project_designer', project_id=project_material_instance.project.id)


def show_scanner_assign_matarial_qr(request):

    return render(request, 'transactions/update_qr_scanner.html')




def update_assign_matarial_qr(request, product_qr_id):

    product_qr_instance = product_qr.objects.get(id = product_qr_id)

    print(request.POST)

    if request.method == "POST":

        a = request.POST.get('size')
        b = request.POST.get('used_size')
        c = request.POST.get('left_size')
        e = request.POST.get('move_to_scratch')
        project_id = request.POST.get('order_id')
        cutter_id = request.POST.get('cutter')

        print('------------------------')

        print(cutter_id)

        try:
            project_instance = project.objects.get(id = project_id)
        except project.DoesNotExist as e:
            msg = "Project with project id:" + project_id
            return JsonResponse({'status' : 'error', 'msg' : msg})


        
        try:
            
            project_material.objects.get(project = project_instance, sheet_no = product_qr_instance.id)

        except project_material.DoesNotExist:
            msg = "Sheet is not assign to project with order id " + project_id + " does not exsisit"
            return JsonResponse({'status' : 'error', 'msg' : msg})



        size_instance1, new_generated_size1 = size.objects.get_or_create(name = a)

        if size_instance1 == None:

            size_instance1 = new_generated_size1


        size_instance2, new_generated_size2 = size.objects.get_or_create(name = b)

        if size_instance2 == None:

            size_instance2 = new_generated_size2


        size_instance3, new_generated_size3= size.objects.get_or_create(name = c)
        
        if size_instance3 == None:

            size_instance3 = new_generated_size3


        project_matarial_qr_instance = project_matarial_qr.objects.filter(product_qr__id = product_qr_id).first()

        product_instance = project_matarial_qr_instance.project_material.product

        cutter_intance = cutter.objects.get(id = cutter_id)

        # Now, retrieve the related project_qr instance
        material_history.objects.create(product_qr = product_qr_instance, previous_size = size_instance1, used_size = size_instance2, left_size = size_instance3, project = project_instance, cutter = cutter_intance)
        
        product_instance_new, product_created_new = product.objects.get_or_create(category = product_instance.category, thickness = product_instance.thickness, size = size_instance3, grade = product_instance.grade)
        
        # project_material_qr_instance = project_matarial_qr.objects.get(product_qr = product_qr_instance)

        # project_material_qr_instance.is_cutting_done = True
        # project_material_qr_instance.save()

        if product_instance_new == None:
            product_instance_new = product_created_new

        if e == "true":

            print(' in scratch ')

            instance, created = scratch_stock.objects.get_or_create(product = product_instance_new)

            if product_qr_instance.moved_to_left_over != True:
            
                stock_instance = stock.objects.get(product = product_instance)
                stock_instance.quantity = stock_instance.quantity - 1
                
                product_qr_instance.moved_to_scratch = True
                product_qr_instance.moved_to_left_over = False
                product_qr_instance.save()

                stock_instance.save()

                if stock_instance.quantity < 4:
                    
                    a1212 = notification_table.objects.create(message =  str(stock_instance.product.category)+ " " + str(stock_instance.product.size)+ " " + str(stock_instance.product.thickness)+ " " + str(stock_instance.product.grade) + "Left :- " + str(stock_instance.quantity))
                    pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                                            key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                                            secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                                            cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                                            ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

                    pusher_client.trigger('alerts', 'new-notificatin', {'message': a1212.message})
              
            else:
                
                left_over_instance =  left_over_stock.objects.get(product = product_qr_instance.product)


                left_over_instance.quantity = left_over_instance.quantity - 1
                left_over_instance.save()

                product_qr_instance.moved_to_scratch = True
                product_qr_instance.save()



            if instance:

                instance.quantity = instance.quantity + 1
                instance.product_qr = product_qr_instance
                instance.save()

            else:

                created.quantity = 1
                created.save()

        else:

            print(' in left over ')


            
            if product_qr_instance.moved_to_left_over != True:
                
                print('----------done----------------')
                print(product_instance)
                instance, created = left_over_stock.objects.get_or_create(product = product_instance_new)
            
                stock_instance = stock.objects.get(product = product_instance)
                stock_instance.quantity = stock_instance.quantity - 1
                stock_instance.save()

                if stock_instance.quantity < 4:
                    
                    a1212 = notification_table.objects.create(message =  str(stock_instance.product.category)+ " " + str(stock_instance.product.size)+ " " + str(stock_instance.product.thickness)+ " " + str(stock_instance.product.grade))
                    pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                                            key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                                            secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                                            cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                                            ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

                    pusher_client.trigger('alerts', 'new-notificatin', {'message': a1212.message})


                product_qr_instance.moved_to_left_over = True
                product_qr_instance.save()

                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.product_qr = product_qr_instance
                    instance.save()

                else:

                    created.quantity = 1
                    created.save()


            else:
                print(product_instance.id)
                left_over_instance = left_over_stock.objects.get(product = product_qr_instance.product)
                left_over_instance.quantity = left_over_instance.quantity - 1
                left_over_instance.save()

                instance, created = left_over_stock.objects.get_or_create(product = product_instance_new)

                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.product_qr = product_qr_instance
                    instance.save()

                else:

                    created.quantity = 1
                    created.save()
        
        
        print('---------------')
        print(product_instance_new)
        print('---------------')

        product_qr_instance.product = product_instance_new
        product_qr_instance.save()
        

        # remove project for this qr
        return JsonResponse({'status' : 'done'})


    else:

        cutter_data = cutter.objects.all()

        context = {
            'data': product_qr_instance,
            'cutter_data': cutter_data,
            'product_qr_id' : product_qr_id
        }

        return render(request, 'transactions/update_assign_material_qr.html', context)


def delete_matarial_history(request, history_id):

    pass

    
from django.forms import modelformset_factory

def add_production(request, project_id):

    project_instance = project.objects.get(id = project_id)

    if request.method == "POST":

        quantity = request.POST.getlist('quantity[]')
        item_code_id = request.POST.getlist('item_code[]')
        material = request.POST.getlist('materialsId[]')
        production_id = request.POST.getlist('production_id[]')
        completed = request.POST.get('completed')


        for a, b, c, d in zip(production_id, item_code_id, quantity, material):

            material_instance = project_matarial_qr.objects.get(id = d)

            if a and a!= '0':

                project_material_instnace = project_matarial_production.objects.get(id = a)
                item_code_instance = item_code.objects.get(id = b)

                project_material_instnace.item_code = item_code_instance
                project_material_instnace.production_quantity = c
                
                project_material_instnace.save()

                print('here')

            else:
                    
                item_code_instance = item_code.objects.get(id = b)
                instance = project_matarial_production.objects.create(project_matarial_qr = material_instance, item_code = item_code_instance, production_quantity = c, project = project_instance)

        if completed == "true":
            project_instance.completed = True
            project_instance.save()

        return JsonResponse({'status' : 'done'})
        
    else:

        data = project_material.objects.filter(project = project_instance)

        item_code_data = item_code.objects.all()

        print(item_code_data)

        # Create the formset with the initial data
       
        context = {
            'form': project_Form(instance=project_instance),
            'data' : data,
            'item_code_data' : item_code_data,
            'project_material_form' : project_matarial_qr_Form(),
            'project_id' : project_id,
        }

        return render(request,'transactions/add_production.html', context )



def delete_production_entry(request, project_id, production_id):


    project_matarial_production.objects.get(id = production_id).delete()

    url = reverse('update_project_accountant', args=[project_id])
    return redirect(url)






import qrcode

from django.core.files.base import ContentFile
from io import BytesIO


import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Image, Spacer
from io import BytesIO


def generate_qr_codes_pdf(qr_codes):
     
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    col_count = 4
    qr_width = 150
    qr_height = 150

    data = []
    row = []
    for qr in qr_codes:
        qr_buffer = BytesIO()
        qr.save(qr_buffer, format='PNG')
        qr_image = Image(qr_buffer)
        qr_image.drawWidth = qr_width
        qr_image.drawHeight = qr_height
        row.append(qr_image)

        if len(row) == col_count:
            data.append(row)
            row = []

    # Add any remaining QR codes to the last row
    if row:
        data.append(row)

    table = Table(data)
    elements.append(table)

    doc.build(elements)

    return buffer


def generate_product_qr(request):

    quantity = request.POST.get('quantity')
    qr_codes = []

    # Specify the desired size in pixels (e.g., 600x600)
    qr_size = 600

    for i in range(int(quantity)):
        
        a = product_qr.objects.create()
        product_qr_shelf.objects.create(product_qr = a)

        # Adjust the box_size based on the desired size
        box_size = qr_size // 4  # You can experiment with different values

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=0,
        )
        qr.add_data(a.id)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white", size=(qr_size, qr_size))
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        qr_code_image = ContentFile(buffer.getvalue())

        a.qr_code.save(f"qr_code_{a.id}.png", qr_code_image)

        qr_codes.append(a)

    context ={
        'data' : qr_codes
    }

    return render(request, 'transactions/html_qr.html', context)
   

def generate_product_qr_with_values(request):

    if request.method == "POST":

        quantity = request.POST.get('quantity')
        shelf_id = request.POST.get('shelf')
        supplier_id = request.POST.get('supplier')
        category_id = request.POST.get('category')
        size_id = request.POST.get('size')
        thickness_id = request.POST.get('thickness')
        grade_id = request.POST.get('grade')
        finish_id = request.POST.get('finish')
        date_of_pur_id = request.POST.get('date_of_pur')


        category_instance = category.objects.get(id = category_id)
        size_instance = size.objects.get(id = size_id)
        thickness_instance = thickness.objects.get(id = thickness_id)
        grade_instance = grade.objects.get(id = grade_id)

        book, created = product.objects.get_or_create(category = category_instance, size =  size_instance, thickness = thickness_instance, grade = grade_instance)
        
        if book:

            product_instance = book

        else:

            product_instance = created

        qr_codes = []

        # Specify the desired size in pixels (e.g., 600x600)
        qr_size = 600

        for i in range(int(quantity)):
            
            instance, created = stock.objects.get_or_create(product = product_instance)
                
            if instance:

                instance.quantity = instance.quantity + 1
                instance.save()
                print('valid4')

            else:

                created.quantity = 1
                created.save()

            supplier_instance= dealer.objects.get(id = supplier_id)

            a = product_qr.objects.create(product = product_instance, date_of_pur = date_of_pur_id, finish = finish_id, supplier = supplier_instance)
            
            shelf_instance = shelf.objects.get(id = shelf_id)
            
            product_qr_shelf.objects.create(product_qr = a, shelf = shelf_instance)

            # Adjust the box_size based on the desired size
            box_size = qr_size // 4  # You can experiment with different values

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=0,
            )
            qr.add_data(a.id)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white", size=(qr_size, qr_size))
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            qr_code_image = ContentFile(buffer.getvalue())

            a.qr_code.save(f"qr_code_{a.id}.png", qr_code_image)

            qr_codes.append(a)

        context ={
            'data' : qr_codes
        }

        return render(request, 'transactions/html_qr.html', context)
    else:

        print('-----------------')
        print('-----------------')
        print('-----------------')
        print('-----------------')
        print('-----------------')

        form = product_Form()
        form_qr = product_qr_Form()
        product_qr_shelf_form = product_qr_shelf_Form()


        context ={
            'form' : form,
            'form_qr': form_qr,
            'product_qr_shelf_form': product_qr_shelf_form,

        }

        return render(request, 'transactions/generate_product_qr_with_values.html', context)


def from_to_generate_product_qr(request):


    from_no = request.POST.get('from')
    to_no = request.POST.get('to')

    qr_codes = []

    # Specify the desired size in pixels (e.g., 600x600)
    qr_size = 600

    for i in range(int(from_no), int(to_no) + 1):
        
        try:
            a = product_qr.objects.get(id = i)
        except product_qr.DoesNotExist:
            a = None
        
        if a:
            # Adjust the box_size based on the desired size
            box_size = qr_size // 4  # You can experiment with different values

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=0,
            )
            qr.add_data(a.id)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white", size=(qr_size, qr_size))
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            qr_code_image = ContentFile(buffer.getvalue())

            a.qr_code.save(f"qr_code_{a.id}.png", qr_code_image)

            qr_codes.append(a)

    context ={
        'data' : qr_codes
    }

    return render(request, 'transactions/html_qr.html', context)
  




from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image


def print_single_qr(request, product_qr_id):

    a = product_qr.objects.get(id = product_qr_id)


    qr_size = 600

    box_size = qr_size // 4  # You can experiment with different values

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=0,
    )
    qr.add_data(a.id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white", size=(qr_size, qr_size))
    buffer = BytesIO()
    img.save(buffer, format="PNG")

    qr_code_image = ContentFile(buffer.getvalue())

    a.qr_code.save(f"qr_code_{a.id}.png", qr_code_image)

    

    return render(request, 'transactions/html_qr_single.html', {'data' : a})

def list_generated_product_qr(request):

    data = product_qr.objects.all().order_by("-id")

    status = request.GET.get('status')
    sheet_id = request.GET.get('sheet_id')

    if sheet_id:
        data = data.filter(id = sheet_id)

    
    elif status:
        data = data.filter(status = status)

    
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        
        'data': data,
        'status': status,
        'sheet_id': sheet_id,
    }

    return render(request, 'transactions/list_all_generated_qr.html', context)
def scanner_page(request):
    
    product_id = request.POST.get('scanned_value')

    context = {
                'product_id': product_id,
        }

    return render(request, 'transactions/scanner.html', context)

def assign_values_to_qr_page(request):

    scanned_value = request.POST.get("scanned_value")

    
    redirect_url = reverse('assign_values_to_qr', args=[scanned_value]) 
    response_data = {'status' : 'success', 'redirect_url': redirect_url}
    return JsonResponse(response_data)
    

def assign_values_to_qr_page_data(request, product_qr_id):

    product_qr_instance = product_qr.objects.get(id = product_qr_id)

    product_form = product_Form(instance = product_qr_instance.product)
    
    context = {
        'form': product_form,
    }

    return render(request, 'transactions/assign_values_to_qr_page_data.html', context)
    

from django.core.files.storage import FileSystemStorage

import copy



def assign_values_to_qr(request, product_qr_id):
    
    print('hereeeeeeee')
    print(product_qr_id)
    product_id = product_qr_id

    try:
        product_qr_instance = product_qr.objects.get(id=product_id)
    except product_qr.DoesNotExist as e:
        # Handle the error and construct an error response
        error_message = str(e)
        return JsonResponse({'status': 'error', 'message': error_message}, status=400)
    
    if request.method == 'POST':

        product_qr_old = product_qr_old = copy.copy(product_qr_instance)

        print('here checking')
        print(product_qr_old.is_fix)

       
        if product_qr_instance.moved_to_left_over == False and product_qr_instance.moved_to_scratch == False:
            print('1111')


            category_id = request.POST.get('category')
            size_id = request.POST.get('size')
            thickness_id = request.POST.get('thickness')
            grade_id = request.POST.get('grade')

            print('printing data ------------------')
           
            print('printing data ------------------')

            category_instance = category.objects.get(id = category_id)
            size_instance = size.objects.get(id = size_id)
            thickness_instance = thickness.objects.get(id = thickness_id)
            grade_instance = grade.objects.get(id = grade_id)

            book, created = product.objects.get_or_create(category = category_instance, size =  size_instance, thickness = thickness_instance, grade = grade_instance)

            print('2222')

            form2 = product_qr_Form(request.POST, request.FILES, instance = product_qr_instance)
            if form2.is_valid():


                print('valid')


                # Save the file to a specific location using FileSystemStorage or another storage backend.
                form2.save()
                shelf_id = request.POST.get('shelf')
                print('----------')
                print(shelf_id)
                print('----------')


                shelf_instance = shelf.objects.get(id = shelf_id)
                product_qr_shelf_instance = product_qr_shelf.objects.get(product_qr = product_qr_instance)
                product_qr_shelf_instance.shelf = shelf_instance
                product_qr_shelf_instance.save()
            
                print('valid2')

                if book:

                    product_instance = book

                else:

                    product_instance = created

                messages.success(request, 'Values added successfully')
                print('valid3')

                
                if product_qr_old.is_fix:

                    instance_previous_stock = stock.objects.get(product = product_qr_old.product)
                    instance_previous_stock.quantity = instance_previous_stock.quantity - 1
                    instance_previous_stock.save()
                
                    if instance_previous_stock.quantity < 4:
                        
                        a1212 = notification_table.objects.create(message =  str(instance_previous_stock.product.category)+ " " + str(instance_previous_stock.product.size)+ " " + str(instance_previous_stock.product.thickness)+ " " + str(instance_previous_stock.product.grade))
                        pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                                                key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                                                secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                                                cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                                                ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

                        pusher_client.trigger('alerts', 'new-notificatin', {'message': a1212.message})

                instance, created = stock.objects.get_or_create(product = product_instance)
                
                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.save()
                    print('valid4')

                else:

                    created.quantity = 1
                    created.save()


                product_qr_instance.product = product_instance
                product_qr_instance.is_fix = True
                product_qr_instance.save()

                redirect_url = reverse('list_generated_product_qr')

                return redirect(redirect_url)

                
            else:

                print(form.errors) 
        else:

            messages.error(request, 'Material already been used please contact pratik')

            return redirect('assign_values_to_qr', product_qr_id=product_qr_id)

    else:    

        form = product_Form(instance=product_qr_instance.product)
        form_qr = product_qr_Form(instance=product_qr_instance)

        print(product_qr_id)
        data = material_history.objects.filter(product_qr__id = product_qr_id)

        product_qr_shelf_instance = product_qr_shelf.objects.get(product_qr = product_qr_instance)

        product_qr_shelf_form = product_qr_shelf_Form(instance = product_qr_shelf_instance)


        context = {
            'form': form,
            'form_qr': form_qr,
            'data': data,
            'sheet_no': product_qr_id,
            'product_qr_id': product_qr_id,
            'project_filter': project_filter(),

            'product_qr_shelf_form': product_qr_shelf_form,
        }

        return render(request, 'transactions/assign_value_to_qr.html', context)
    
def delete_history(request, history_id):

    material_history_instance = material_history.objects.get(id = history_id)

    product_qr_instance = material_history_instance.product_qr

    product_old = copy.copy(product_qr_instance.product)

    obj, created = product.objects.get_or_create(category_id = product_qr_instance.product.category.id, size_id = material_history_instance.previous_size, grade_id = product_qr_instance.product.grade.id, thickness_id = product_qr_instance.product.thickness.id)

    if obj:
        product_qr_instance.product = obj
        product_qr_instance.save()
    else:
        product_qr_instance.product = created
        product_qr_instance.save()


    if product_qr_instance.moved_to_scratch:

        print('runung 1')

        material_history_count = material_history.objects.filter(product_qr = product_qr_instance).count()
        
        instance_previous_stock = scratch_stock.objects.get(product = product_old)
        instance_previous_stock.quantity = instance_previous_stock.quantity - 1
        instance_previous_stock.save()
        
        if material_history_count == 1:

            print('22')  

            instance, created = stock.objects.get_or_create(product = product_qr_instance.product)

            if instance:

                instance.quantity = instance.quantity + 1
                instance.save()

            else:

                created.quantity = 1
                created.save()

            product_qr_instance.moved_to_scratch = False
            product_qr_instance.moved_to_left_over = False
            product_qr_instance.save()

        else:

            print('11')  
            

            product_qr_instance.moved_to_scratch = False
            product_qr_instance.moved_to_left_over = True
            product_qr_instance.save()

            instance, created = left_over_stock.objects.get_or_create(product = product_qr_instance.product)

            if instance:

                instance.quantity = instance.quantity + 1
                instance.save()

            else:

                created.quantity = 1
                created.save()

    


    elif product_qr_instance.moved_to_left_over:

        print('runung 2')

        material_history_count = material_history.objects.filter(product_qr = product_qr_instance).count()

        instance_previous_stock = left_over_stock.objects.get(product = product_old)
        instance_previous_stock.quantity = instance_previous_stock.quantity - 1
        instance_previous_stock.save()

        if material_history_count == 1:

            instance, created = stock.objects.get_or_create(product = product_qr_instance.product)

            if instance:

                instance.quantity = instance.quantity + 1
                instance.save()

            else:

                created.quantity = 1
                created.save()

            product_qr_instance.moved_to_scratch = False
            product_qr_instance.moved_to_left_over = False
            product_qr_instance.save()

        else:
            
            instance, created = left_over_stock.objects.get_or_create(product = product_qr_instance.product)

            if instance:

                instance.quantity = instance.quantity + 1
                instance.save()

            else:

                created.quantity = 1
                created.save()



    material_history_instance.delete()

    return redirect('list_generated_product_qr')



def assign_values_to_qr_page(request):

    scanned_value = request.POST.get("scanned_value")


    redirect_url = reverse('assign_values_to_qr', args=[scanned_value]) 
    response_data = {'status' : 'success', 'redirect_url': redirect_url}
    return JsonResponse(response_data)


def update_product(request, product_id):

    pass

def verify_password(request):

    
    emplpyee_id = request.POST.get("employee")
    password = request.POST.get("password")

    employee_instance = employee.objects.get(id = emplpyee_id)

    if employee_instance.password == password:

        return JsonResponse({'status' : "done"})
    
    else:

        return JsonResponse({'status' : "wrong"})

