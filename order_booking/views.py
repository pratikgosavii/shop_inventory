from django.shortcuts import get_object_or_404, render

# Create your views here.

from transactions.models import *
from transactions.forms import *

import pusher
from django.conf import settings
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


from store.views import numOfDays
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from store.forms import *


def add_order_booking(request):


    item_code_data = item_code.objects.filter(status = True)


    if request.method == 'POST':

        print(request.POST)
        print(request.FILES)

        # Deserialize the JSON data into a Python object
        forms = order_booking_Form(request.POST, request.FILES, user=request.user)

        order_id = request.POST.get("order_id")
       

        item_code_id = request.POST.getlist('item_code')
        category_id = request.POST.getlist('category')
        grade_id = request.POST.getlist('grade')
        thickness_id = request.POST.getlist('thickness')
        quantity = request.POST.getlist('production_quantity')
        new_row_tokens = request.POST.getlist('new_row_token')
        production_id = request.POST.getlist('production_id')

        print('-----------------')
        print('-----------------')
        print(quantity)
        print(item_code_id)
        print(production_id)

        print('-----------------')
        print('-----------------')

        if forms.is_valid():

            order_instance = forms.save()

            print('valid')

            for a, b, c, d, e, f, token in zip(production_id, item_code_id, category_id, grade_id, thickness_id, quantity, new_row_tokens):

                print('in form')

                if not b.strip():  # skip row if item_code is blank
                    continue

                if a and a!= '0':

                    project_material_instnace = order_matarial_production.objects.get(id = a)
                    # handle drawings files (multiple)
                    file_field_name = f'drawings_{a}'   # input name="drawings_{{ i.id }}"
                    for uploaded_file in request.FILES.getlist(file_field_name):
                        order_matarial_production_drawing.objects.create(
                            production=project_material_instnace,
                            file=uploaded_file
                        )

                    item_code_instance = item_code.objects.get(id = b)
                    category_instance = category.objects.get(id = c)
                    grade_instance = grade.objects.get(id = d)
                    thickness_instance = thickness.objects.get(id = e)

                    project_material_instnace.item_code = item_code_instance
                    project_material_instnace.category = category_instance
                    project_material_instnace.grade = grade_instance
                    project_material_instnace.thickness = thickness_instance
                    project_material_instnace.production_quantity = f
                    
                    project_material_instnace.save()

                    print('here')

                else:

                    print('here3')

                        
                    item_code_instance = item_code.objects.get(id = b)
                    category_instance = category.objects.get(id = c)
                    grade_instance = grade.objects.get(id = d)
                    thickness_instance = thickness.objects.get(id = e)

                    instance = order_matarial_production.objects.create(
                        item_code=item_code_instance,
                        category=category_instance,
                        grade=grade_instance,
                        thickness=thickness_instance,
                        production_quantity=f,
                        order=order_instance
                    )
                    # attach drawings for this new row using its token
                    if token:
                        file_field_name_new = f'drawings_{token}'
                        for uploaded_file in request.FILES.getlist(file_field_name_new):
                            order_matarial_production_drawing.objects.create(
                                production=instance,
                                file=uploaded_file
                            )

            system_alert.objects.create(role="designer", message="New job assigned", is_active = True)

            # a1212 = alert.objects.create(message = "New Order Registered ID " + order_id)
            # pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
            #                           key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
            #                           secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
            #                           cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
            #                           ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

            # pusher_client.trigger('alerts', 'new-alert', {'message': a1212.message})

            return redirect('list_order_booking')


        else:
                
            print(forms.errors)
            
            data_form = product_Form()

            context = {
                'form': forms,
                'item_code_data': item_code_data,
                'data_form': data_form,
            }
            return render(request, 'transactions/add_order_booking.html', context)


    else:

        forms = order_booking_Form(user=request.user)
        data_form = product_Form()

        context = {
            'form': forms,
            'data_form': data_form,
            'item_code_data': item_code_data,
        }
        return render(request, 'transactions/add_order_booking.html', context)
    


def update_order_booking(request, order_id):

    order_booking_instance = order_booking.objects.get(id = order_id)

    if request.method == 'POST':

        print(request.POST)

        # Deserialize the JSON data into a Python object
        forms = order_booking_Form(request.POST, request.FILES, instance=order_booking_instance, user=request.user)


      
        order_id = order_booking_instance.order_id
       
        quantity = request.POST.getlist('production_quantity')
        item_code_id = request.POST.getlist('item_code')

        category_id = request.POST.getlist('category')
        grade_id = request.POST.getlist('grade')
        thickness_id = request.POST.getlist('thickness')
        production_id = request.POST.getlist('production_id')
        new_row_tokens = request.POST.getlist('new_row_token')


        print('-----------------------')
        print(production_id)
        print(quantity)
        print(item_code_id)
        print(category_id)
        print(grade_id)
        print(thickness_id)


        if forms.is_valid():

            print('is valid')

            order_instance = forms.save()


            # no-op: per-row files handled via unique new_row_token now

            for a, b, c, d, e, f, token in zip(production_id, item_code_id, category_id, grade_id, thickness_id, quantity, new_row_tokens):

                print('----------')
                print(a)
                if not b.strip():  # skip row if item_code is blank
                    continue
                
                if a and a != '0':

                    project_material_instnace = order_matarial_production.objects.get(id = a)

                    item_code_instance = item_code.objects.get(id = b)
                    category_instance = category.objects.get(id = c)
                    grade_instance = grade.objects.get(id = d)
                    thickness_instance = thickness.objects.get(id = e)
                    
                    project_material_instnace.item_code = item_code_instance
                    project_material_instnace.production_quantity = f
                    
                    project_material_instnace.category = category_instance
                    project_material_instnace.grade = grade_instance
                    project_material_instnace.thickness = thickness_instance

                    file_field_name = f'drawings_{a}'   # input name="drawings_{{ i.id }}"
                    for uploaded_file in request.FILES.getlist(file_field_name):
                        order_matarial_production_drawing.objects.create(
                            production=project_material_instnace,
                            file=uploaded_file
                        )


                    project_material_instnace.save()

                    print('here')

                else:

                    print('------------in else ----------------')
                        
                    item_code_instance = item_code.objects.get(id = b)
                    category_instance = category.objects.get(id = c)
                    grade_instance = grade.objects.get(id = d)
                    thickness_instance = thickness.objects.get(id = e)

                    instance = order_matarial_production.objects.create(
                        item_code=item_code_instance,
                        category=category_instance,
                        grade=grade_instance,
                        thickness=thickness_instance,
                        production_quantity=f,
                        order=order_instance
                    )
                    # attach drawings for this new row using its token
                    if token:
                        file_field_name_new = f'drawings_{token}'
                        for uploaded_file in request.FILES.getlist(file_field_name_new):
                            order_matarial_production_drawing.objects.create(
                                production=instance,
                                file=uploaded_file
                            )

                
            system_alert.objects.create(role="designer", message="New job assigned", is_active = True)

            # a1212 = alert.objects.create(message = "Order Updated  ID " + order_id)
            # pusher_client = pusher.Pusher(app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
            #                           key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
            #                           secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
            #                           cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
            #                           ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"])

            # pusher_client.trigger('alerts', 'new-alert', {'message': a1212.message})

            return redirect('list_order_booking')


        else:
                
            print(forms.errors)
            
            data_form = product_Form()

            context = {
                'form': forms,
                'item_code_data': item_code_data,
                'data_form': data_form,
                'order_id': order_id,
            }
            return render(request, 'transactions/add_order_booking.html', context)


    else:

        forms = order_booking_Form(instance=order_booking_instance, user=request.user)

        production_data = order_matarial_production.objects.filter(order = order_booking_instance)

        item_code_data = item_code.objects.filter(status = True)
        data_form = product_Form()

        context = {
            'form': forms,
            'data_form': data_form,
            'production_data': production_data,
            'item_code_data': item_code_data,
            'order_id': order_id,
        }
        return render(request, 'transactions/add_order_booking.html', context)
    




from django.db import transaction

def update_order_booking_designer(request, order_id):
    order_booking_instance = order_booking.objects.get(id=order_id)

    if request.method == 'POST':
        print(request.POST)

        forms = order_booking_Form(
            request.POST, request.FILES,
            instance=order_booking_instance,
            user=request.user
        )

        production_id = request.POST.getlist('production_id')
        size_values = request.POST.getlist('size')
        total_size = sum(float(val) for val in size_values if val.strip())

        print('-----------------------')
        print(production_id)
        print(size_values)

        if forms.is_valid():
            print('is valid')

            try:
                with transaction.atomic():  # 🔹 wrap all DB ops in one transaction

                    forms.save()

                    # update related material productions
                    for a, b in zip(production_id, size_values):
                        print('----------')
                        print(a, b)

                        if not a.strip() or not b.strip():
                            print('skippp')
                            continue

                        instance = order_matarial_production.objects.get(id=a)
                        instance.size = b

                        # handle drawings files (multiple)
                        file_field_name = f'drawings_{a}'   # input name="drawings_{{ i.id }}"
                        for uploaded_file in request.FILES.getlist(file_field_name):
                            order_matarial_production_drawing.objects.create(
                                production=instance,
                                file=uploaded_file
                            )

                        instance.save()

                    # update total size on order
                    order_booking_instance.total_sqinch = total_size
                    order_booking_instance.save()

                    print("✅ Order & productions updated")

                    # create alert
                    a1212 = alert.objects.create(message=f"Order Updated  ID {order_id}")
                    
                    
                    # system_alert.objects.create(role="designer", message="New job assigned", is_active = True)

                    # # push notification
                    # pusher_client = pusher.Pusher(
                    #     app_id=settings.PUSH_NOTIFICATIONS_SETTINGS["APP_ID"],
                    #     key=settings.PUSH_NOTIFICATIONS_SETTINGS["KEY"],
                    #     secret=settings.PUSH_NOTIFICATIONS_SETTINGS["SECRET"],
                    #     cluster=settings.PUSH_NOTIFICATIONS_SETTINGS["CLUSTER"],
                    #     ssl=settings.PUSH_NOTIFICATIONS_SETTINGS["USE_TLS"]
                    # )
                    # pusher_client.trigger('alerts', 'new-alert', {'message': a1212.message})

                # 🔹 if all good, redirect
                return redirect('list_order_booking')

            except Exception as e:
                # rollback happens automatically if exception is raised
                print(f"❌ Error in update_order_booking_designer: {e}")
                forms.add_error(None, f"Something went wrong: {str(e)}")

        else:
            print(forms.errors)

        # If invalid form or exception -> render page again
        data_form = product_Form()
        item_code_data = item_code.objects.filter(status=True)
        production_data = order_matarial_production.objects.filter(order=order_booking_instance)

        context = {
            'form': forms,
            'data_form': data_form,
            'item_code_data': item_code_data,
            'production_data': production_data,
            'order_id': order_id,
        }
        return render(request, 'transactions/update_order_booking.html', context)

    else:
        forms = order_booking_Form(instance=order_booking_instance, user=request.user)
        production_data = order_matarial_production.objects.filter(order=order_booking_instance)
        item_code_data = item_code.objects.filter(status=True)
        data_form = product_Form()

        context = {
            'form': forms,
            'item_code_data': item_code_data,
            'order_id': order_id,
            'production_data': production_data,
            'data_form': data_form,
        }
        return render(request, 'transactions/update_order_booking.html', context)
    
    
    


def update_production_order(request, production_order_id):

    production_order_instance = production_orders.objects.get(id = production_order_id)

    if request.method == 'POST':

        print(request.POST)
        post_data = request.POST.copy()
        post_data["order"] = production_order_instance.order.id  # force the FK

        forms = production_orders_Form(
            post_data,
            request.FILES,
            instance=production_order_instance
        )

        if forms.is_valid():

            print('is valid')

            forms.save()


            return redirect('dashboard_working_order')


        else:
                
            
           
            context = {
                'form': forms,
            }
            return render(request, 'transactions/update_production_order.html', context)


    else:

        forms = production_orders_Form(instance=production_order_instance)

        context = {
            'form': forms,
        }
        return render(request, 'transactions/update_production_order.html', context)
    



def delete_order_booking(request, order_id):

    order_booking_instance = order_booking.objects.get(id = order_id)

    order_booking_instance.delete()

    return redirect('list_order_booking')


    
@login_required(login_url='login')
def list_order_booking(request):

  
    data = order_booking.objects.all().order_by("-id")

    
    filterset = order_booking_filter(request.GET, queryset=data, request=request)
    data = filterset.qs

    
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
        'filterset': filterset,
        'order_booking_filter': order_booking_filter(),
       
    }

    return render(request, 'transactions/list_orders_booking.html', context)

    
@login_required(login_url='login')
def delete_order_production(request, production_id):

    instance = order_matarial_production.objects.get(id = production_id)

    order_id = instance.order.is_drawing_avaiable
    instance.delete()
    
    return redirect('update_order_booking', order_id = order_id)

@login_required(login_url='login')
def delete_order_sheet_requiremnt(request, order_sheet_id):

    instance = order_matarial_production.objects.get(id = order_sheet_id)

    order_id = instance.order.is_drawing_avaiable
    instance.delete()
    
    return redirect('update_order_booking_designer', order_id = order_id)


from django.utils import timezone 

def move_to_production(request, order_id):

    order = get_object_or_404(order_booking, id=order_id)

    # 2. Check if already moved to production

    a = production_orders.objects.filter(order = order)
    if a:
        messages.warning(request, f"Order {order.order_id} is already in production.")
        return redirect("list_order_booking")  # adjust url name

    # 3. Create production order

    priority = production_orders.objects.filter(stage="in_progress").count()
    production = production_orders.objects.create(
        order=order,
        priority=priority+2,  # default medium priority (or get from request.POST if form)
        stage="in_progress",
        start_date=timezone.now().date(), 
    )

    # 4. Update order status
    order.status = "in_progress"
    order.save()

    messages.success(request, f"Order {order.order_id} moved to production successfully.")
    return redirect('dashboard_working_order')   # change to your order list view name

def move_to_planning(request, order_id):

    order = get_object_or_404(order_booking, id=order_id)

    # 2. Check if already moved to production

    
    # 4. Update order status
    order.status = "planning"
    order.design_completion_date = timezone.now().date()
    order.save()

    messages.success(request, f"Order {order.order_id} moved to production successfully.")
    return redirect('list_order_booking')   # change to your order list view name

def mark_as_completed(request, production_id):

    order = get_object_or_404(production_orders, id=production_id)

    # 2. Check if already moved to production
    order.stage="completed",
    order.save()

    instance = order.order
    instance.status = "completed"
    instance.actual_end_date = timezone.now().date()
    instance.save()
       

    messages.success(request, f"Order {order.order_id} order marked completed successfully.")
    return redirect('dashboard_working_order')   # change to your order list view name

def mark_as_hold(request, production_id):

    order = get_object_or_404(production_orders, id=production_id)

    if request.method == "POST":
        hold_reason = request.POST.get("hold_reason")  # get value from modal form

        if hold_reason:
            order.stage = "hold"
            order.hold_reason = hold_reason
            order.save()

            # update related order status
            instance = order.order
            instance.status = "hold"
            instance.save()

            messages.success(request, f"Order {order.id} has been moved to hold (Reason: {hold_reason}).")
        else:
            messages.error(request, "Please select a hold reason before submitting.")

    return redirect("dashboard_executor_order")

def active_production_order(request, production_id):

    order = get_object_or_404(production_orders, id=production_id)


    order.stage = "in_progress"
    order.save()
    
    booking_order_instance = order.order
    booking_order_instance.status = "in_progress"
    booking_order_instance.save()

      

    
    return redirect("dashboard_working_order")




@login_required(login_url='login')
def production_list(request):

  
    data = production_orders.objects.all().order_by("-id")

    
   
    context = {
        'data': data,
       
    }

    return render(request, 'working_order_dashboard.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # If you're using CSRF protection, don't forget to handle the token
def update_priority(request):
    if request.method == "POST":
        print('--------1-----------------')
        try:
            print('--------2-----------------')

            data = json.loads(request.body)
            order = data.get("order", [])
            print(data)
            print(order)
            for item in order:
                obj_id = item.get("id")
                position = item.get("position")
                production_orders.objects.filter(id=obj_id).update(priority=position)

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "invalid request"}, status=405)



@login_required(login_url='login')
def order_today_report(request):

    data = order_booking.objects.filter(updated_at = date.today()).order_by("-id")

    # ✅ Prepare default filter values if not provided in GET
    get_data = request.GET.copy()

      # default status

    if "date" not in get_data:
        get_data["date"] = date.today().strftime("%Y-%m-%d")  # default today's date

    # ✅ Apply filter
    filterset = order_booking_filter(get_data, queryset=data, request=request)
    data = filterset.qs

    # ✅ Pagination
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
        'filterset': filterset,
        'order_booking_filter': order_booking_filter(get_data),  # pass defaults to template also
    }

    return render(request, 'transactions/order_today_report.html', context)
