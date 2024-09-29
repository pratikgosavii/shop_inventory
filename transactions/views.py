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

   
    data = stock.objects.filter(quantity__gt=0).prefetch_related('product__project_material_re').order_by('product__category', 'product__grade')
    
    
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
        return render(request, 'transactions/add_sales_customer.html', context)

        

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
        return render(request, 'transactions/add_sales_customer.html', context)



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
        return render(request, 'transactions/add_sales_customer.html', context)

        

@login_required(login_url='login')
def delete_sales_customer(request, sales_customer_id):

    sales_customer.objects.get(id=sales_customer_id).delete()

    return HttpResponseRedirect(reverse('list_sales_customer'))


        

def gettoken(request):


    return render(request, 'transactions/gettoken.html')


@login_required(login_url='login')
def list_sales_customer(request):

    data = sales_customer.objects.all()

    context = {
        'data': data
    }

    return render(request, 'transactions/list_sales_customer.html', context)

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
import requests


def send_notification():


    # Define the URL
    url = "https://fcm.googleapis.com/fcm/send"

    # Define the payload
    payload = {
        "notification": {
            "body": "This is an FCM notification message!",
            "time": "FCM Message"
        },
        "registration_ids": [
            "deXBxhh5kaaduGWQn-XIWH:APA91bF6HOf_sdv0yLfgxKKhxr0V-ilVOzPtFEbU9MLhFyKISQDdOvFCVuA0dihoXvuB94iAXsBOOYWEz7i6o9u90e9NWDd3a5KeH8ANQQrnoFiXopO95-VBvM2X0b53EEIA3g4ZXV3l"
        ]
    }

    # Define the headers
    headers = {
        "Authorization": "key=AAAA-aJPhnk:APA91bGsRiq0bVsPc2DUPDWxiJvNOvdYpkcPG9pAT2V0aUzmNBws7O5uzdVOtCiY6d-7QrJ1PTGN2pTUenPIbL7ZB6qIwYomhsOHyaipHLlMT4dbFgKVTIb1yO6zsdkUC0aJLF7G7_8B",
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.text)





import http.client
import ssl 


access_token = "EAALeGznz5UwBO9cCf9mrwEd1vHBgB8neIziWXhS4AKGY02ZCVbfb5bTnSK7TCX6Qo1V0MZCHg7hNHQJYsNIZB17zlXaXFLv4HWJFWHZA0zeK57eZCClKyKxeAROKBh0kWB9PtjGbJeJsDWQSdqIjr20xrOBvk09nfWZCRn4xi5MTuyhco7C3U9P4OZBRbADDzLfKwZDZD"
recipient_number = ["8237377298"]
template_name = "qutation_added"
language_code = "en"

def send_qutation_notification(request, token, recipient_number, template_name, language_code, parameter_value):


    print('-----------------------------------------------')
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    print('-----------------------------------------------')

    url = "https://graph.facebook.com/v20.0/363920080139942/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    for number in recipient_number:
        payload = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                },
                "components": [
                    {
                        "type": "button",
                        "sub_type": "url",
                        "index": 0,
                        "parameters": [
                            {
                                "type": "text",
                                "text": parameter_value
                            }
                        ]
                    }
                ]
            }
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200:
            print(f"Error sending message to {number}: {response.status_code}")
            print(f"Response: {response.text}")
        else:
            print(f"Message sent to {number}: {response}")





def send_low_stock_notification(request, token, recipient_number, template_name, language_code, dynamic_value):


    url = "https://graph.facebook.com/v20.0/363920080139942/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {
                "code": language_code
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": dynamic_value
                        }
                    ]
                }
            ]
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response)
    return response.json()

def work_alert(request, token, recipient_number, template_name, language_code, param1, param2):

    
    url = "https://graph.facebook.com/v20.0/363920080139942/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {
                "code": language_code
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": param1
                        },
                        {
                            "type": "text",
                            "text": param2
                        }
                    ]
                }
            ]
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.json())


    return response.json()

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

            return JsonResponse({'status' : 'done', 'instance' : forms.instance.item_code})


        else:

            print(forms_order.errors)

      
        
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

        


        
def send_notification():


    # Define the URL
    url = "https://fcm.googleapis.com/fcm/send"

    # Define the payload
    payload = {
        "notification": {
            "body": "This is an FCM notification message!",
            "time": "FCM Message"
        },
        "registration_ids": [
            "deXBxhh5kaaduGWQn-XIWH:APA91bF6HOf_sdv0yLfgxKKhxr0V-ilVOzPtFEbU9MLhFyKISQDdOvFCVuA0dihoXvuB94iAXsBOOYWEz7i6o9u90e9NWDd3a5KeH8ANQQrnoFiXopO95-VBvM2X0b53EEIA3g4ZXV3l"
        ]
    }

    # Define the headers
    headers = {
        "Authorization": "key=AAAA-aJPhnk:APA91bGsRiq0bVsPc2DUPDWxiJvNOvdYpkcPG9pAT2V0aUzmNBws7O5uzdVOtCiY6d-7QrJ1PTGN2pTUenPIbL7ZB6qIwYomhsOHyaipHLlMT4dbFgKVTIb1yO6zsdkUC0aJLF7G7_8B",
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.text)





from django.forms.models import model_to_dict

import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone


@login_required(login_url='login')
def update_order(request, order_id):

    instance = order.objects.get(id = order_id)

    if request.method == 'POST':

        print('-----------------------')
        print('-----------------------')
        print('-----------------------')
        print('-----------------------')
        print('-----------------------')

        orders_data_json = request.POST.get('orders', '[]')
        deletedOrderIdss = request.POST.get('deletedOrderIds')
        orders_data = json.loads(orders_data_json)
        deleted_order_ids = json.loads(deletedOrderIdss)

        print(deleted_order_ids)

        for i in deleted_order_ids:

            print(i)

            order_child.objects.get(id = i).delete()

        updated_request = request.POST.copy()
        updated_request.update({'user': request.user})

        print(request.POST)
        forms_order = order_Form(updated_request, instance = instance)

        if forms_order.is_valid():

            forms_order.save()

            for item in orders_data:


                order_child_instance = order_child.objects.get(id = item['pk'])
                item['order'] = forms_order.instance.id
                
                forms = OrderChildForm(item, instance = order_child_instance)
                if forms.is_valid():

                    forms.save()



                else:

                    return JsonResponse({'status' : 'error'})

        
            return JsonResponse({'status' : 'done', 'instance' : forms.instance.item_code})


        else:

            print(forms_order.errors)

      
        
    else:


        instance = order.objects.get(id=order_id)
        forms = order_Form(instance=instance)
        order_child_instance = order_child.objects.filter(order=instance)
        order_child_instance_copy = copy.copy(order_child_instance)
        # Convert date fields to string representations
        instance_dict = model_to_dict(instance)
        order_child_instance_list = [model_to_dict(child) for child in order_child_instance]

        print(order_child_instance_copy)


        
        context = {
            'form': forms,
            'instance': instance,
            'order_child_instance_dict': json.dumps(order_child_instance_list, cls=DjangoJSONEncoder),
            'instance_json': json.dumps(instance_dict, cls=DjangoJSONEncoder),  # Convert instance to JSON string
            'order_child_instance_copy': order_child_instance_copy,  # Convert instance to JSON string
        }
        return render(request, 'transactions/update_order.html', context)

        

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

    return render(request, 'transactions/list_orders.html', context)

def print_order(request, order_id):

    order_data = order.objects.get(id = order_id)
    order_child_data = order_child.objects.filter(order = order_data)

    print(order_child_data)

    
    context = {
        'order_data': order_data,
        'order_child_data': order_child_data
    }

    return render(request, 'transactions/print_orders.html', context)


def approve_order(request, order_id):

    order_instance = order.objects.get(id = order_id)
    order_instance.is_approved = True
    order_instance.save()

    return redirect('list_order')




# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        subscription_data = json.loads(request.body)
        # Store subscription_data in your database
        return JsonResponse({'success': True})





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
from django.conf import settings



from datetime import datetime, timedelta



def script(request):


    a = project.objects.filter(completed = False)

    message_body = ""

    for i in a:

        b = project_material.objects.filter(project = i)

        for z in b:

            product_qr_instance = product_qr.objects.get(id = z.sheet_no)

            current_date = datetime.now().date()
            two_days_ago = current_date - timedelta(days=2)

            # Check if the given date has exceeded 2 days from the current date
            if i.DC_date < two_days_ago:

                c = material_history.objects.filter(product_qr = product_qr_instance, project = i)

                if not c:

                    print('messae--------------------------------------')
                    
                    message_body += "Update: Prjoect Id: " + str(i.id) + " " + "Customer Name: " + str(i.customer.name) + "Sheet No " + str(z.sheet_no)

                            
                    work_alert(request, access_token, recipient_number, 'sheet_update', language_code, message_body, z.id)

    return JsonResponse({'message': 'response message'}, status=400)






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


from openpyxl import Workbook
from openpyxl.styles import Font
import os



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

            print('valid')


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
                    instance = project_matarial_production.objects.create(item_code = item_code_instance, project = project_instance, production_quantity = c)

                

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
        length = request.POST.getlist("length")
        width = request.POST.getlist("width")

        print('-----------------')

        print(length)
        print(width)

        filtered_values = project_material.objects.filter(project = project_instance).values_list('sheet_no', flat=True)

        existing_values = [int(value) for value in filtered_values]

        # Find values that are unique to value_list
        sheet_no_id = [int(value) for value in sheet_no_id]

        unique_values = [value for value in sheet_no_id if value not in existing_values]

        print(existing_values)
        print(sheet_no_id)
        print(unique_values)

        if forms.is_valid():
            

           


          
            project_instance = forms.save()

            if unique_values != ['']:

                print('in')
                for a, b, c in zip(unique_values, length, width):
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

                    project_material_instance = project_material.objects.create(product = product_id, project = project_instance, quantity = 1, sheet_no = a, length = b, width = c)

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
def confirm_outward(request, project_id):

    project_instance = project.objects.get(id = project_id)
    

    forms = project_Form(instance = project_instance)
                

    production_data = project_matarial_production.objects.filter(project = project_instance)
    

    context = {
        'form': forms,
        'production_data': production_data,
        'project_id': project_id,
    }
    return render(request, 'transactions/confirm_outward.html', context)



@login_required(login_url='login')
def confirm_outward_json(request, production_material_id):

    instance = project_matarial_production.objects.get(id = production_material_id)

    instance.date_time = datetime.now()

    instance.save()

    return redirect('confirm_outward', project_id = instance.project.id)


@login_required(login_url='login')
def add_project_inward(request, project_id):

    project_instance = project.objects.get(id = project_id)
    
    if request.method == 'POST':

        invoice_no = request.POST.getlist("invoice_no")
        title = request.POST.getlist("title")
        quantity = request.POST.getlist("quantity")
        description = request.POST.getlist("description1")
        date = request.POST.getlist("DC_date")



        print(request.POST)
        print(invoice_no)
        print(title)
        print(quantity)
        print(description)
        print(date)


        for a,b,c,d,e,f in zip(invoice_no, title, quantity, description, date):

            project_inward.objects.create(project = project_instance, invoice_no = a, title = b, quantity = c, description = e, date = f)

        
        return redirect('list_project')



@login_required(login_url='login')
def add_project_outward(request, project_id):

    project_instance = project.objects.get(id = project_id)
    
    if request.method == 'POST':

        invoice_no = request.POST.getlist("invoice_no")
        title = request.POST.getlist("title")
        quantity = request.POST.getlist("quantity")
        description = request.POST.getlist("description1")
        date = request.POST.getlist("DC_date")



        print(request.POST)
        print(invoice_no)
        print(title)
        print(quantity)
        print(description)
        print(date)


        for a,b,c,d,e,f in zip(invoice_no, title, quantity, description, date):

            project_outward.objects.create(project = project_instance, invoice_no = a, title = b, quantity = c, description = e, date = f)

            print('here')



        return redirect('list_project')

    else:

        forms = project_Form(instance = project_instance)
                    
        data_form = project_outward_Form()

        data_inward = project_inward.objects.filter(project = project_instance)
        data_outward = project_outward.objects.filter(project = project_instance)

        
        context = {
            'form': forms,
            'data_inward': data_inward,
            'data_outward': data_outward,
        }
        return render(request, 'transactions/add_project_outward.html', context)




from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import mm


def generate_barcode(request, id):
    
    data = project_matarial_production.objects.get(id=id)

    # Create a PDF buffer with 45mm x 25mm page size
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=(50 * mm, 30 * mm))

    # Set the barcode value
    barcode_value = str(data.id)
    
    # Increase the barcode width (barWidth increased, height kept standard)
    barcode = code128.Code128(barcode_value, barWidth=0.45 * mm, barHeight=10 * mm)

    # Set the position of the barcode (minimal margins)
    barcode_x = 1  # 1mm from the left
    barcode_y = 16  # Adjust position slightly from the bottom

    # Draw the barcode on the PDF
    barcode.drawOn(pdf, barcode_x * mm, barcode_y * mm)

    # Optional: Add text below the barcode with smaller font size and reduced line spacing
    pdf.setFont("Helvetica", 5)  # Set font size to 5 points

    # Reduce line spacing and remove unnecessary info (SIZE removed)
    pdf.setFont("Helvetica-Bold", 5)  # Set font size to 5 points, bold font for weight
    left_margin = 1 * mm  # Adjust left margin as needed
    pdf.drawString(left_margin, (barcode_y - 3) * mm, f"Project ID: {data.project.order_id} | Quantity: {data.production_quantity}")
    pdf.drawString(left_margin, (barcode_y - 6) * mm, f"Item Code: {data.item_code.code}")
    pdf.drawString(left_margin, (barcode_y - 9) * mm, f"Company Name: {data.project.customer.name}")
    pdf.drawString(left_margin, (barcode_y - 12) * mm, f"Name: Ravi-Raj Anodisers")

    # Finalize the PDF
    pdf.showPage()
    pdf.save()

    # Get the PDF content
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="barcode_{id}.pdf"'

    return response




def generate_all_barcode(request, project_id):
    # Choose the type of barcode you want to generate (e.g., Code128)
    
    
    
    ids_list = project_matarial_production.objects.filter(project__id = project_id)
    pdf_buffer = BytesIO()
    
    # Create the PDF
    pdf = canvas.Canvas(pdf_buffer, pagesize=(45 * mm, 25 * mm))
    
    for id in ids_list:
        data = project_matarial_production.objects.get(id=id.id)
        
        # Set the barcode value
        barcode_value = str(data.id)
        
        # Increase the barcode width (barWidth increased, height kept standard)
        barcode = code128.Code128(barcode_value, barWidth=0.45 * mm, barHeight=10 * mm)
        
        # Set the position of the barcode (minimal margins)
        # Set the position of the barcode (minimal margins)
        barcode_x = 1  # 1mm from the left
        barcode_y = 16  # Adjust position slightly from the bottom

        # Draw the barcode on the PDF
        barcode.drawOn(pdf, barcode_x * mm, barcode_y * mm)

        # Optional: Add text below the barcode with smaller font size and reduced line spacing
        pdf.setFont("Helvetica", 5)  # Set font size to 5 points

        # Reduce line spacing and remove unnecessary info (SIZE removed)
        pdf.setFont("Helvetica-Bold", 5)  # Set font size to 5 points, bold font for weight
        left_margin = 1 * mm  # Adjust left margin as needed
        pdf.drawString(left_margin, (barcode_y - 3) * mm, f"Project ID: {data.project.order_id} | Quantity: {data.production_quantity}")
        pdf.drawString(left_margin, (barcode_y - 6) * mm, f"Item Code: {data.item_code.code}")
        pdf.drawString(left_margin, (barcode_y - 9) * mm, f"Company Name: {data.project.customer.name}")
        pdf.drawString(left_margin, (barcode_y - 12) * mm, f"Name: Ravi-Raj Anodisers")
            
        # Start a new page for the next barcode
        pdf.showPage()
    
    # Finalize the PDF
    pdf.save()
    
    # Get the PDF content
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="barcodes.pdf"'
    
    return response

def scan_barcode(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        
        try:
            # Look up the product by the scanned barcode
            product = project_matarial_production.objects.get(id=barcode)

            return redirect('confirm_outward', project_id=product.project.id)

        
        except project_outward.DoesNotExist:
            return HttpResponse("Product not found.")
    
    return render(request, 'transactions/scan_barcode.html')  # Return scan page if no POST data




@login_required(login_url='login')
def add_inward(request):


    if request.method == 'POST':

        
        # Deserialize the JSON data into a Python object
        forms = project_inward_Form(request.POST, request.FILES)
        

        if forms.is_valid():

            forms.save()

            return redirect('list_inward')


        else:
                
            print(forms.errors)
            
            data_form = project_inward_Form()

            context = {
                'form': forms,
                'data_form': data_form,
            }
            return render(request, 'transactions/add_inward.html', context)


    else:

        forms = project_inward_Form()

        context = {
            'form': forms,
        }
        return render(request, 'transactions/add_inward.html', context)
    

@login_required(login_url='login')
def update_inward(request, inward_id):

    instance = project_inward.objects.get(id = inward_id)


    if request.method == 'POST':

        
        # Deserialize the JSON data into a Python object
        forms = project_inward_Form(request.POST, instance=instance)
        

        if forms.is_valid():

            forms.save()

            return redirect('list_inward')


        else:
                
            print(forms.errors)
            
            data_form = project_inward_Form(instance=instance)

            context = {
                'form': forms,
                'data_form': data_form,
            }
            return render(request, 'transactions/add_inward.html', context)


    else:

        forms = project_inward_Form(instance=instance)

        context = {
            'form': forms,
        }
        return render(request, 'transactions/add_inward.html', context)
    



@login_required(login_url='login')
def list_inward(request):

    data = project_inward.objects.all().order_by('-id')

    data = project_inward_filter(request.GET, queryset=data)

    data = data.qs

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
        'project_filter': project_inward_filter(request.GET),
       
    }
    


    return render(request, 'transactions/list_inward.html', context)



@login_required(login_url='login')
def delete_inward(request, inward_id):

    project_inward.objects.get(id = inward_id).delete()


    return redirect('list_inward')



@login_required(login_url='login')
def inward_report(request):


    data = project_inward.objects.all().order_by("-project")

    
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
        'project_inward_filter': project_inward_filter(),
       
    }

    return render(request, 'transactions/list_project_inward_report.html', context)




def download_inward_report(request):

      
    data = project_inward.objects.all()
    project_inward_filters = project_inward_filter(request.GET, queryset=data)
    project_inward_filters_data1 = list(project_inward_filters.qs.values_list('customer', 'quantity', 'description', 'date'))
    project_inward_filters_data = list(map(list, project_inward_filters_data1))

    # Create an Excel workbook and sheet
    wb = Workbook()
    ws = wb.active
    ws.title = 'Inward Report'

    # Header information
    ws.append([''])  # Empty row
    ws.append(['Inward Report'])  # Title row
    ws.append([''])  # Empty row
    ws.append([''])  # Empty row

    # Add table headers
    headers = ["Sr No", "Customer", "Quantity", "Description", "Date"]
    ws.append(headers)

    # Apply light green color to header row
    light_green_fill = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")

    for cell in ws[ws.max_row]:  # Select the last added row (header row)
        cell.fill = light_green_fill

    # Append data to the Excel file
    counteer = 1
    for i in project_inward_filters_data:
        ws.append([counteer, i[0], i[1], i[2], i[3]])
        counteer += 1

    # Save the workbook to a BytesIO stream
    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    # Create a response for the file download
    response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Inward_Report.xlsx"'

    return response


def download_inward_report_pdf(request):

      
    data = project_inward.objects.all()
    project_inward_filters = project_inward_filter(request.GET, queryset=data)
    project_inward_filters_data1 = list(project_inward_filters.qs.values_list('customer', 'quantity', 'description', 'date'))
    project_inward_filters_data = list(map(list, project_inward_filters_data1))

    # Add serial numbers to the data
    formatted_data = [[idx + 1] + row for idx, row in enumerate(project_inward_filters_data)]

    # Prepare the table data with headers
    table_data = [['Sr No', 'Customer', 'Quantity', 'Description', 'Date']]  # Header row
    table_data.extend(formatted_data)

    # Set up the PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Define the styles for the heading
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    
    # Create the title
    title = Paragraph("Inward Report", title_style)

    # Spacer between the title and table
    spacer = Spacer(1, 20)

    # Create the table
    table = Table(table_data)

    # Add styling to the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all text
        ('BACKGROUND', (1, 1), (-1, -1), colors.whitesmoke),  # Data row background
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borders for table cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header
    ]))

    # Build the PDF
    elements = [title, spacer, table]
    doc.build(elements)

    # Prepare PDF as response
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf', headers={
        'Content-Disposition': 'attachment; filename="inward_report.pdf"'
    })



@login_required(login_url='login')
def outward_report(request):


    project_filter_data = project_filter(request.GET, queryset=project.objects.all())
    production_filter = project_matarial_production_filter(request.GET, queryset=project_matarial_production.objects.all())


    print(request.GET)

    # Apply production filter and prefetch the filtered production data
    project_qs = project_filter_data.qs  # Ensure this is a queryset
    production_qs = production_filter.qs  # Ensure this is a queryset

    print(production_qs)
    print(project_qs)

    # Prefetch the production data using the correct related_name for the relationship
    projects = project_qs.filter(
        project_production_n__in=production_qs  # Ensures only projects with related filtered production records
    ).prefetch_related(
        Prefetch('project_production_n', queryset=production_qs)  # Prefetch the filtered production data
    ).distinct()

    data = projects

    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print(projects)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    for i in data:
        totals = i.project_production_n.aggregate(
            total_quantity=Sum('production_quantity'),
        )
        
        # Add totals to i instance for template access
        i.total_quantity = totals['total_quantity'] or 0


    context = {
        'data': data,
        'project_filter': project_filter(request.GET),
        'project_matarial_production_filter': project_matarial_production_filter(request.GET),
       
    }

      

   


    return render(request, 'transactions/list_project_outward_report.html', context)



from openpyxl.styles import PatternFill, Font, Border, Side
import os
import mimetypes
from django.http import HttpResponse
from django.db.models import Sum



from django.core.mail import EmailMessage




def outward_report_csv(request):

# Query data
    projects = project.objects.all().order_by("-id")

     # Check if request.GET is empty
    if is_invalid_get_params(request.GET):
        # Create a mutable copy of request.GET
        default_params = QueryDict(mutable=True)
        
        # Set default parameters

        default_params.update({
        'from_date_time': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) - timedelta(days=1),
        'to_date_time': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
        })

    else:

        default_params = request.GET
                
    project_filter_data = project_filter(default_params, queryset=project.objects.all())
    production_filter = project_matarial_production_filter(default_params, queryset=project_matarial_production.objects.all())


    print(default_params)

    # Apply production filter and prefetch the filtered production data
    project_qs = project_filter_data.qs  # Ensure this is a queryset
    production_qs = production_filter.qs  # Ensure this is a queryset

    print(production_qs)
    print(project_qs)

    # Prefetch the production data using the correct related_name for the relationship
    projects = project_qs.filter(
        project_production_n__in=production_qs  # Ensures only projects with related filtered production records
    ).prefetch_related(
        Prefetch('project_production_n', queryset=production_qs)  # Prefetch the filtered production data
    ).distinct()

    data = projects

    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Define styles
    light_green_fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
    light_orange_fill = PatternFill(start_color='FFDAB9', end_color='FFDAB9', fill_type='solid')
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'),
                         top=Side(style='thin'), bottom=Side(style='thin'))
    bold_font = Font(bold=True)

    # Apply borders to a range of cells in bulk
    def apply_borders_range(start_row, end_row):
        for row in ws.iter_rows(min_row=start_row, max_row=end_row):
            for cell in row:
                if cell.value:  # Only apply borders to non-empty cells
                    cell.border = thin_border

    # Write the main table header
    ws.append(["Material outward", "", "", "", ""])
    ws.append(["#", "Date", "Project Order No", "RRA Invoice No", "Customer Name"])

    # Apply background color to header cells of the main table
    for cell in ws[2]:
        cell.fill = light_green_fill

    row_index = 3

    # Write rows for each project
    for project_instance in data:
        ws.append([])  # Blank row for spacing

        # Write the project row
        ws.append([
            str(project_instance.pk),
            str(project_instance.DC_date),
            str(project_instance.order_id),
            str(project_instance.rra_invoice_no),
            str(project_instance.customer)
        ])

        # Write nested table header for project productions
        ws.append(["", "Item Code", "Quantity"])
        for cell in ws[ws.max_row]:
            cell.fill = light_orange_fill

        # Write project production rows
        productions = project_instance.project_production_n.all()
        for i in productions:
            ws.append([
                "", 
                str(i.item_code), 
                str(i.production_quantity), 
            ])

        # Calculate totals
        totals = project_instance.project_production_n.aggregate(
            total_quantity=Sum('production_quantity'),
        )
        total_quantity = totals['total_quantity'] or 0

        # Write the totals row
        ws.append([
            "", 
            "Project Total", 
            str(total_quantity), 
        ])
        for cell in ws[ws.max_row]:
            cell.font = bold_font

        # Apply borders only after writing all rows
        apply_borders_range(row_index, ws.max_row)

        # Update the row index
        row_index = ws.max_row + 2

    # Save and return the workbook
    name = 'outward_report_with_optimized_colors.xlsx'
    link = os.path.join(BASE_DIR, 'static', 'csv', name)
    wb.save(link)

    mime_type, _ = mimetypes.guess_type(link)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    # with open(link, 'rb') as f:
    #     response = HttpResponse(f.read(), content_type=mime_type)
    #     response['Content-Disposition'] = f'attachment; filename="{name}"'

     # Save the workbook to an in-memory file (BytesIO)
    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    # Create the response
    response = HttpResponse(
        excel_file.getvalue(), 
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="outward_report.xlsx"'
    
    return response



from io import BytesIO
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from django.shortcuts import render
from .models import project
from django.db.models import Sum
import os
from reportlab.lib.units import cm

from django.http import QueryDict



def is_invalid_get_params(get_params):
    # Check if 'undefined' exists and has no value, or if the GET request is empty
    return not get_params or ('undefined' in get_params and len(get_params['undefined']) == 0)



from django.db.models import Prefetch


def generate_outward_report_pdf(request):

     # Filter projects and production based on request parameters
    project_filter = project_filter(request.GET, queryset=project.objects.all())
    production_filter = project_matarial_production_filter(request.GET, queryset=project_matarial_production.objects.filter(date_time__gte=yesterday_6pm, date_time__lte=today_6pm))
    
    # Apply production filter and prefetch the filtered production data
    projects = project_filter.qs.prefetch_related(
        Prefetch('project_production_n', 
                 queryset=production_filter.qs)
    ).distinct()

    context = {
        'projects': projects,
        'project_filter': project_filter,
        'production_filter': production_filter
    }
    
    return render(request, 'report_template.html', context)


def generate_outward_report_daily_pdf(request):
    # Create an in-memory buffer for the PDF file
    
   
    # Create an in-memory buffer for the PDF file
    buffer = BytesIO()

    # Create a PDF document with minimal margins
    pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )
    
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.alignment = 1  # Centered

    # Title of the PDF
    title = Paragraph("Material Outward Report", title_style)
    elements.append(title)

    # Query data from the database
    projects = project.objects.all().order_by("-id")

     # Check if request.GET is empty
        # Create a mutable copy of request.GET
        
        # Set default parameters
                
    yesterday_6pm = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) - timedelta(days=1)
    today_6pm = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)


    # Prefetch production data related to projects with filtering
    projects = project.objects.prefetch_related(
        Prefetch('project_production_n', 
                queryset=project_matarial_production.objects.filter(date_time__gte=yesterday_6pm, date_time__lte=today_6pm))
    ).filter(project_production_n__date_time__gte=yesterday_6pm, project_production_n__date_time__lte=today_6pm).distinct()

    print(projects)

      
        # Update the parameters
      


    light_orange = colors.Color(1, 0.647, 0, alpha=1)  # RGB for light orange

    for project_instance in projects:
        # Data for the main table
        main_table_data = [
            ["#", "Date", "Project Order No", "RRA Invoice No", "Customer Name"],
            [
                str(project_instance.pk),
                str(project_instance.DC_date),
                str(project_instance.order_id),
                str(project_instance.rra_invoice_no),
                str(project_instance.customer),
            ]
        ]

        # Create the main table
        main_table = Table(main_table_data)
        main_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),  # Header row background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (1, 1), (-1, -1), colors.whitesmoke),  # Data row background
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borders for table cells
        ]))

        elements.append(main_table)

        # Add an empty line for separation
        elements.append(Paragraph(''))

        # Nested table data
        nested_table_data = [
            ["#", "Item Code", "Quantity"]
        ]

        # Add data rows for each production
        productions = project_instance.project_production_n.all()
        for counter, production in enumerate(productions, start=1):
            nested_table_data.append([
                str(counter),
                str(production.item_code),
                str(production.production_quantity),
            ])

        # Add totals for this project
        totals = project_instance.project_production_n.aggregate(
            total_quantity=Sum('production_quantity'),
        )
        total_quantity = totals['total_quantity'] or 0
        nested_table_data.append([
            "",
            "Project Total",
            str(total_quantity),
        ])

        # Create the nested table
        nested_table = Table(nested_table_data, colWidths=[40, 200, 100, 100])  # Adjusted width for Item Code
        nested_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), light_orange),  # Header row background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (1, 1), (-1, -1), colors.whitesmoke),  # Data row background
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borders for table cells
        ]))

        # Center the nested table within the page
        elements.append(Paragraph(''))  # Add a blank line for separation
        elements.append(nested_table)

        # Add an extra empty line for spacing between projects
        elements.append(Paragraph(''))


        # Add a blank line
        elements.append(Spacer(1, 0.5 * cm))



    # Build the PDF into the buffer
    pdf.build(elements)

    file_path = os.path.join(settings.MEDIA_ROOT, 'outward_report.pdf')


    with open(file_path, 'wb') as f:
        f.write(buffer.getvalue())

    # Close the buffer
    buffer.close()

    return file_path




# Function to send the PDF as an email attachment
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
from django.http import HttpResponse

from django.http import HttpResponse
from django.conf import settings
import os




def generate_inward_report_daily_pdf(request):


    default_params = QueryDict(mutable=True)
    
    # Set default parameters

    default_params.update({
    'from_date_time': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) - timedelta(days=1),
    'to_date_time': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
    })

    data = project_inward.objects.all()
    project_inward_filters = project_inward_filter(default_params, queryset=data)
    project_inward_filters_data1 = list(project_inward_filters.qs.values_list('customer', 'quantity', 'description', 'date'))
    project_inward_filters_data = list(map(list, project_inward_filters_data1))

    # Add serial numbers to the data
    formatted_data = [[idx + 1] + row for idx, row in enumerate(project_inward_filters_data)]

    # Prepare the table data with headers
    table_data = [['Sr No', 'Customer', 'Quantity', 'Description', 'Date']]  # Header row
    table_data.extend(formatted_data)

    # Set up the PDF file path
    name = "inward_report.pdf"
    file_path = os.path.join(settings.BASE_DIR, 'static', 'reports', name)  # Ensure the 'static/reports/' directory exists

    # Create the PDF document and save it to the specified path
    doc = SimpleDocTemplate(file_path, pagesize=letter)

    # Define the styles for the heading
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    
    # Create the title
    title = Paragraph("Inward Report", title_style)

    # Spacer between the title and table
    spacer = Spacer(1, 20)

    # Create the table
    table = Table(table_data)

    # Add styling to the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all text
        ('BACKGROUND', (1, 1), (-1, -1), colors.whitesmoke),  # Data row background
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borders for table cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header
    ]))

    # Build the PDF
    elements = [title, spacer, table]
    doc.build(elements)

    # Return the file path
    return file_path

def send_outward_report_pdf_email_daily(request):
    # Generate and save the PDF
    
    
    file_path = generate_outward_report_daily_pdf(request)
    file_path2 = generate_inward_report_daily_pdf(request)

    # Create the email
    email = EmailMessage(
        subject='Outward Report PDF',
        body='Please find the attached outward report in PDF format.',
        from_email='rradailyupdates@gmail.com',
        # to=['varad@ravirajanodisers.com', 'ravi@ravirajanodisers.com', 'pratikgosavi654@gmail.com', 'raj@ravirajanodisers.com'],
        to=['pratikgosavi654@gmail.com'],
    )

    # Attach the generated PDF
    email.attach_file(file_path)
    email.attach_file(file_path2)

    # Send the email
    email.send()

    return HttpResponse("Email with PDF attachment sent successfully.")




def generate_outward_report_pdf_email(request):
    # Create an in-memory buffer for the PDF file
    
   
    # Create an in-memory buffer for the PDF file
    buffer = BytesIO()

    # Create a PDF document with minimal margins
    pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )
    
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.alignment = 1  # Centered

    # Title of the PDF
    title = Paragraph("Material Outward Report", title_style)
    elements.append(title)

    # Query data from the database
    projects = project.objects.all().order_by("-id")

     # Check if request.GET is empty
    if is_invalid_get_params(request.GET):
        # Create a mutable copy of request.GET
        default_params = QueryDict(mutable=True)
        
        # Set default parameters

        default_params.update({
        'from_date_time': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) - timedelta(days=1),
        'to_date_time': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
        })

    else:

        default_params = request.GET
                
    project_filter_data = project_filter(default_params, queryset=project.objects.all())
    production_filter = project_matarial_production_filter(default_params, queryset=project_matarial_production.objects.all())


    print(default_params)

    # Apply production filter and prefetch the filtered production data
    project_qs = project_filter_data.qs  # Ensure this is a queryset
    production_qs = production_filter.qs  # Ensure this is a queryset

    print(production_qs)
    print(project_qs)

    # Prefetch the production data using the correct related_name for the relationship
    projects = project_qs.filter(
        project_production_n__in=production_qs  # Ensures only projects with related filtered production records
    ).prefetch_related(
        Prefetch('project_production_n', queryset=production_qs)  # Prefetch the filtered production data
    ).distinct()



      
        # Update the parameters
      


    light_orange = colors.Color(1, 0.647, 0, alpha=1)  # RGB for light orange

    for project_instance in projects:
        # Data for the main table
        main_table_data = [
            ["#", "Date", "Project Order No", "RRA Invoice No", "Customer Name"],
            [
                str(project_instance.pk),
                str(project_instance.DC_date),
                str(project_instance.order_id),
                str(project_instance.rra_invoice_no),
                str(project_instance.customer),
            ]
        ]

        # Create the main table
        main_table = Table(main_table_data)
        main_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),  # Header row background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (1, 1), (-1, -1), colors.whitesmoke),  # Data row background
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borders for table cells
        ]))

        elements.append(main_table)

        # Add an empty line for separation
        elements.append(Paragraph(''))

        # Nested table data
        nested_table_data = [
            ["#", "Item Code", "Quantity"]
        ]

        # Add data rows for each production
        productions = project_instance.project_production_n.all()
        for counter, production in enumerate(productions, start=1):
            nested_table_data.append([
                str(counter),
                str(production.item_code),
                str(production.production_quantity),
            ])

        # Add totals for this project
        totals = project_instance.project_production_n.aggregate(
            total_quantity=Sum('production_quantity'),
        )
        total_quantity = totals['total_quantity'] or 0
        nested_table_data.append([
            "",
            "Project Total",
            str(total_quantity),
        ])

        # Create the nested table
        nested_table = Table(nested_table_data, colWidths=[40, 200, 100, 100])  # Adjusted width for Item Code
        nested_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), light_orange),  # Header row background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (1, 1), (-1, -1), colors.whitesmoke),  # Data row background
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borders for table cells
        ]))

        # Center the nested table within the page
        elements.append(Paragraph(''))  # Add a blank line for separation
        elements.append(nested_table)

        # Add an extra empty line for spacing between projects
        elements.append(Paragraph(''))


        # Add a blank line
        elements.append(Spacer(1, 0.5 * cm))



    # Build the PDF into the buffer
    pdf.build(elements)

    file_path = os.path.join(settings.MEDIA_ROOT, 'outward_report.pdf')


    with open(file_path, 'wb') as f:
        f.write(buffer.getvalue())

    # Close the buffer
    buffer.close()

    return file_path







def send_outward_report_pdf_email(request):
    # Generate and save the PDF
    
    
    file_path = generate_outward_report_pdf_email(request)

    # Create the email
    email = EmailMessage(
        subject='Outward Report PDF',
        body='Please find the attached outward report in PDF format.',
        from_email='rradailyupdates@gmail.com',
        # to=['varad@ravirajanodisers.com', 'ravi@ravirajanodisers.com', 'pratikgosavi654@gmail.com', 'raj@ravirajanodisers.com'],
        to=['pratikgosavi654@gmail.com'],
    )

    # Attach the generated PDF
    email.attach_file(file_path)

    # Send the email
    email.send()

    return HttpResponse("Email with PDF attachment sent successfully.")


from django.http import FileResponse



def download_outward_report_pdf(request):
    # Generate and save the PDF
    
    
    
    
    file_path = generate_outward_report_pdf_email(request)  # Assuming this function generates the PDF and returns the file path
    
    # Open the file in binary mode for reading
    pdf_file = open(file_path, 'rb')
    
    # Return the file as a downloadable response
    response = FileResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="outward_report.pdf"'
    
    return response






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

        print('1111111111')
        
        try:
            
            project_material.objects.get(project = project_instance, sheet_no = product_qr_instance.id)

        except project_material.DoesNotExist:
            msg = "Sheet is not assign to project with order id " + project_id + " does not exsisit"
            return JsonResponse({'status' : 'error', 'msg' : msg})

        print('22222222222222')


        size_instance1, new_generated_size1 = size.objects.get_or_create(name = a)

        if size_instance1 == None:

            size_instance1 = new_generated_size1

        print('333333333333333')

        size_instance2, new_generated_size2 = size.objects.get_or_create(name = b)

        if size_instance2 == None:

            size_instance2 = new_generated_size2


        size_instance3, new_generated_size3= size.objects.get_or_create(name = c)
        
        if size_instance3 == None:

            size_instance3 = new_generated_size3


        print('4444444444')


        project_matarial_qr_instance = project_matarial_qr.objects.filter(product_qr__id = product_qr_id).first()

        product_instance = project_matarial_qr_instance.project_material.product

        cutter_intance = cutter.objects.get(id = cutter_id)

        # Now, retrieve the related project_qr instance
        c = material_history.objects.create(product_qr = product_qr_instance, previous_size = size_instance1, used_size = size_instance2, left_size = size_instance3, project = project_instance, cutter = cutter_intance)
        product_instance_new, product_created_new = product.objects.get_or_create(category = product_instance.category, thickness = product_instance.thickness, size = size_instance3, grade = product_instance.grade)
        



        print('555555555555555')





        project_material_qr_instance = project_matarial_qr.objects.get(product_qr = product_qr_instance, project_material = project_matarial_qr_instance.project_material)
        

        project_material_qr_instance.is_cutting_done = True
        project_material_qr_instance.save()

        if product_instance_new == None:
            product_instance_new = product_created_new


        print('666666666666666666666666')

        if e == "true":

            print(' in scratch ')

            instance, created = scratch_stock.objects.get_or_create(product = product_instance_new)

            if product_qr_instance.moved_to_left_over != True:


                print('----------------------------------2----------------------')

                print(product_instance.id)
                stock_instance = stock.objects.get(product = product_instance)
                stock_instance.quantity = stock_instance.quantity - 1
                
                product_qr_instance.moved_to_scratch = True
                product_qr_instance.moved_to_left_over = False
                product_qr_instance.save()

                stock_instance.save()

                
                check_low_stock = stock.objects.filter(product__category = stock_instance.product.category, product__thickness = stock_instance.product.thickness).aggregate(total_quantity=Sum('quantity'))
                print(check_low_stock)
                total_quantity = check_low_stock['total_quantity'] or 0  # Handle None case
                print(total_quantity)
                if total_quantity < 5:
                    

                    print('-------------------1------------------')


             
                    
                    message_body =  str(stock_instance.product.category) + " " +str(stock_instance.product.thickness)+ " " + str(stock_instance.product.grade) + " " + str(total_quantity) + " "

                                    
                   
                    send_low_stock_notification(request, access_token, recipient_number, 'stock_alert', language_code, message_body)
                    

                    
              
            else:

                print('-------------------2------------------')

                
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

                
                check_low_stock = stock.objects.filter(product__category = stock_instance.product.category, product__thickness = stock_instance.product.thickness).aggregate(total_quantity=Sum('quantity'))
                print(check_low_stock)
                total_quantity = check_low_stock['total_quantity'] or 0  # Handle None case
                print(total_quantity)
                if total_quantity < 5:

                    print('------------------1----------------------')

                    

                    message_body =  str(stock_instance.product.category) + " " +str(stock_instance.product.thickness)+ " " + str(stock_instance.product.grade) + " " + str(total_quantity) + " "


                                    
                   
                    send_low_stock_notification(request, access_token, recipient_number, 'stock_alert', language_code, message_body)



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







def get_cutting_values(request):

    project_id = request.GET.get('project_id')
    product_qr_id = request.GET.get('sheet_id')
    product_qr_instance = product_qr.objects.get(id = product_qr_id)

    data = project_material.objects.get(project = project_id, sheet_no = product_qr_instance.id)

    used_sqinch = data.length * data.width
    used_sqinch += used_sqinch / (25.4 * 25.4)



    # Round to 2 decimal places
    used_sqinch = round(used_sqinch, 2)

    data = {
        'length': data.length,  # Replace with actual field names
        'width': data.width,    # Replace with actual field names
        'used_sqinch': used_sqinch  # Example calculation
    }


    

    return JsonResponse(data)


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

def print_label(request, project_id, product_qr_id):

    project_instance = project.objects.get(id = project_id)

    data = project_material.objects.get(project = project_id, sheet_no = product_qr_id)

   
    context = {
        
        'project_id': project_id,
        'product_qr_id': product_qr_id,
        # 'sqinch_alloted': product_qr_id,
        'date': datetime.now(),
        'project_name': project_instance.customer,
        'cutting_size': data,
    }

    

    return render(request, 'transactions/html_print_label.html', {'data' : context})

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



def check_sheet(request):

    data = product_qr.objects.all()

    for i in data:

        if i.moved_to_left_over == "None"  and i.moved_to_scratch == "None":
            if i.product:
                print(i.id, ' ', i.moved_to_left_over, ' ', i.moved_to_scratch, ' ', 'True', ' ', i.product.size)
        else:
            if i.product:
                print(i.id, ' ', i.moved_to_left_over, ' ', i.moved_to_scratch, ' ', 'False', ' ', i.product.size)



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

