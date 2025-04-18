from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import *
from .forms import *
from .models import *

from datetime import date

from datetime import datetime
from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib import messages


import pytz
ist = pytz.timezone('Asia/Kolkata')



def numOfDays(date1):

    dt1 = date1.split('T')

    time = dt1[1]

    dt1 = dt1[0]
    
    dt1 = dt1.split('-')
    

    year = int(dt1[0])
    month = int(dt1[1])
    day = int(dt1[2])

    date1 = datetime(year,month, day, tzinfo=ist)

    return date1


@login_required(login_url='login')
def add_godown(request):

    if request.method == 'POST':

        forms = godown_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_godown')
        else:
            print(forms.errors)
    
    else:

        forms = godown_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_godown.html', context)

        

@login_required(login_url='login')
def update_godown(request, godown_id):

    if request.method == 'POST':

        instance = shelf.objects.get(id=godown_id)

        forms = godown_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_godown')
        else:
            print(forms.errors)
    
    else:

        instance = shelf.objects.get(id=godown_id)
        forms = godown_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_godown.html', context)

        

@login_required(login_url='login')
def delete_godown(request, godown_id):

    shelf.objects.get(id=godown_id).delete()

    return HttpResponseRedirect(reverse('list_godown'))


        

@login_required(login_url='login')
def list_godown(request):

    data = godown.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_godown.html', context)

@login_required(login_url='login')
def add_item_code(request):

    if request.method == 'POST':

        forms = item_code_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_item_code')
        else:
            print(forms.errors)
    
    else:

        forms = item_code_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_item_code.html', context)

        

@login_required(login_url='login')
def activate_item_code(request, item_code_id):


    instance = item_code.objects.get(id=item_code_id)

    instance.status = 1
    instance.save()

    return redirect('list_item_code')

@login_required(login_url='login')
def deactivate_item_code(request, item_code_id):


    instance = item_code.objects.get(id=item_code_id)

    instance.status = 0
    instance.save()

    return redirect('list_item_code')


@login_required(login_url='login')
def update_item_code(request, item_code_id):

    if request.method == 'POST':

        instance = item_code.objects.get(id=item_code_id)

        forms = item_code_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_item_code')
        else:
            print(forms.errors)
    
    else:

        instance = item_code.objects.get(id=item_code_id)
        forms = item_code_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_item_code.html', context)

        

@login_required(login_url='login')
def delete_item_code(request, item_code_id):

    item_code.objects.get(id=item_code_id).delete()

    return HttpResponseRedirect(reverse('list_item_code'))


        

@login_required(login_url='login')
def list_item_code(request):

    data = item_code.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_item_code.html', context)


@login_required(login_url='login')
def add_customer(request):

    if request.method == 'POST':

        forms = customer_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_customer')
        else:
            print(forms.errors)
    
    else:

        forms = customer_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_customer.html', context)

        

@login_required(login_url='login')
def update_customer(request, customer_id):

    if request.method == 'POST':

        instance = customer.objects.get(id=customer_id)

        forms = customer_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_customer')
        else:
            print(forms.errors)
    
    else:

        instance = customer.objects.get(id=customer_id)
        forms = customer_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_customer.html', context)

        

@login_required(login_url='login')
def delete_customer(request, customer_id):

    customer.objects.get(id=customer_id).delete()

    return HttpResponseRedirect(reverse('list_customer'))


@login_required(login_url='login')
def list_customer(request):

    data = customer.objects.all()
    context = {
        'data': data
    }
    return render(request, 'store/list_customer.html', context)

@login_required(login_url='login')
def add_employee(request):

    if request.method == 'POST':

        forms = employee_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee')
        else:
            print(forms.errors)
    
    else:

        forms = employee_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_employee.html', context)

        

@login_required(login_url='login')
def update_employee(request, employee_id):

    if request.method == 'POST':

        instance = employee.objects.get(id=employee_id)

        forms = employee_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee')
        else:
            print(forms.errors)
    
    else:

        instance = employee.objects.get(id=employee_id)
        forms = employee_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_employee.html', context)

        

@login_required(login_url='login')
def delete_employee(request, employee_id):

    employee.objects.get(id=employee_id).delete()

    return HttpResponseRedirect(reverse('list_employee'))


@login_required(login_url='login')
def list_employee(request):

    data = employee.objects.all()
    context = {
        'data': data
    }
    return render(request, 'store/list_employee.html', context)

@login_required(login_url='login')
def add_cutter(request):

    if request.method == 'POST':

        forms = cutter_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_cutter')
        else:
            print(forms.errors)
    
    else:

        forms = cutter_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_cutter.html', context)

        

@login_required(login_url='login')
def update_cutter(request, cutter_id):

    if request.method == 'POST':

        instance = cutter.objects.get(id=cutter_id)

        forms = cutter_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_cutter')
        else:
            print(forms.errors)
    
    else:

        instance = cutter.objects.get(id=cutter_id)
        forms = cutter_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_cutter.html', context)

        

@login_required(login_url='login')
def delete_cutter(request, cutter_id):

    cutter.objects.get(id=cutter_id).delete()

    return HttpResponseRedirect(reverse('list_cutter'))


@login_required(login_url='login')
def list_cutter(request):

    data = cutter.objects.all()
    context = {
        'data': data
    }
    return render(request, 'store/list_cutter.html', context)

        

@login_required(login_url='login')
def list_godown(request):

    data = shelf.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_godown.html', context)


@login_required(login_url='login')
def add_dealer(request):

    if request.method == 'POST':

        forms = dealer_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_dealer')
        else:
            print(forms.errors)
    
    else:

        forms = dealer_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_dealer.html', context)

        

@login_required(login_url='login')
def update_dealer(request, dealer_id):

    if request.method == 'POST':

        instance = dealer.objects.get(id=dealer_id)

        forms = dealer_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_dealer')
        else:
            print(forms.errors)
    
    else:

        instance = dealer.objects.get(id=dealer_id)
        forms = dealer_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_dealer.html', context)

        

@login_required(login_url='login')
def delete_dealer(request, dealer_id):

    dealer.objects.get(id=dealer_id).delete()

    return HttpResponseRedirect(reverse('list_dealer'))


        

@login_required(login_url='login')
def list_dealer(request):

    data = dealer.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_dealer.html', context)



@login_required(login_url='login')
def add_category(request):
    
    if request.method == 'POST':

        forms = category_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_category')
        else:
            print(forms.errors)
            return redirect('add_category')
    
    else:

        forms = category_Form()

            
       
        context = {
            'form': forms,
           
        }

        return render(request, 'store/add_category.html', context)


def update_category(request, category_id):

    if request.method == 'POST':

        instance = category.objects.get(id=category_id)

        forms = category_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_category')

        else:
            print(forms.errors)
    
    else:

        instance = category.objects.get(id=category_id)

        forms = category_Form(instance = instance)


        context = {
            'form': forms,
            
        }

        return render(request, 'store/add_category.html', context)


@login_required(login_url='login')
def delete_category(request, category_id):
    
    category.objects.get(id=category_id).delete()

    return HttpResponseRedirect(reverse('list_category'))


@login_required(login_url='login')
def list_category(request):

    
     
    data = category.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_category.html', context)



@login_required(login_url='login')
def add_size(request):
    
    if request.method == 'POST':

        forms = size_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_size')
        else:
            print(forms.errors)
            return redirect('list_size')
    
    else:

        forms = size_Form()
        
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_size.html', context)

@login_required(login_url='login')
def update_size(request, update_size_id):

    if request.method == 'POST':

        instance = size.objects.get(id=update_size_id)

        forms = size_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_size')
    
    else:

        instance = size.objects.get(id=update_size_id)

        

        forms = size_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_size.html', context)


@login_required(login_url='login')
def delete_size(request, thickness_id):
    
    size.objects.get(id=thickness_id).delete()

    return HttpResponseRedirect(reverse('list_size'))


@login_required(login_url='login')
def list_size(request):
    
     
    data = size.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_size.html', context)

from .forms import inward_supplier_Form

@login_required(login_url='login')
def add_inward_supplier(request):
    
    if request.method == 'POST':

        forms = inward_supplier_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_inward_supplier')
        else:
            print(forms.errors)
            return redirect('list_inward_supplier')
    
    else:

        forms = inward_supplier_Form()
        
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_inward_supplier.html', context)

@login_required(login_url='login')
def update_inward_supplier(request, update_inward_supplier_id):

    if request.method == 'POST':

        instance = inward_supplier.objects.get(id=update_inward_supplier_id)

        forms = inward_supplier_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_inward_supplier')
    
    else:

        instance = inward_supplier.objects.get(id=update_inward_supplier_id)

        

        forms = inward_supplier_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_inward_supplier.html', context)


@login_required(login_url='login')
def delete_inward_supplier(request, thickness_id):
    
    inward_supplier.objects.get(id=thickness_id).delete()

    return HttpResponseRedirect(reverse('list_inward_supplier'))


@login_required(login_url='login')
def list_inward_supplier(request):
    
     
    data = inward_supplier.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_size.html', context)



@login_required(login_url='login')
def add_grade(request):
    
    if request.method == 'POST':

        forms = grade_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade')
        else:
            print(forms.errors)
            return redirect('list_grade')
    
    else:

        forms = grade_Form()
      
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_grade.html', context)

@login_required(login_url='login')
def update_grade(request, company_goods_id):

    if request.method == 'POST':

        instance = grade.objects.get(id=company_goods_id)

        forms = grade_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade')
    
    else:

        instance = grade.objects.get(id=company_goods_id)

        

        forms = grade_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_grade.html', context)


@login_required(login_url='login')
def delete_grade(request, grade_id):
    
    grade.objects.get(id=grade_id).delete()

    return HttpResponseRedirect(reverse('list_grade'))


@login_required(login_url='login')
def list_grade(request):
    
     
    data = grade.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_grade.html', context)

@login_required(login_url='login')
def add_thickness(request):
    
    if request.method == 'POST':

        forms = thickness_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_thickness')
        else:
            print(forms.errors)
            return redirect('list_thickness')
    
    else:

        forms = thickness_Form()
        
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_thickness.html', context)

@login_required(login_url='login')
def update_thickness(request, thickness_id):

    if request.method == 'POST':

        instance = thickness.objects.get(id=thickness_id)

        forms = thickness_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_thickness')
    
    else:

        instance = thickness.objects.get(id=company_goods_id)

        

        forms = thickness_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_thickness.html', context)


@login_required(login_url='login')
def delete_thickness(request, thickness_id):
    
    thickness.objects.get(id=thickness_id).delete()

    return HttpResponseRedirect(reverse('list_thickness'))


@login_required(login_url='login')
def list_thickness(request):
    
    data = thickness.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_thickness.html', context)




# delete view





from django.http import JsonResponse
from .models import SheetCut
import json

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import SheetCut  # your model

@csrf_exempt
@login_required(login_url='login')
def draw_sheet(request, sheet_id):
        
    context = {
        "sheet_id" : sheet_id
    }
        
    return render(request, 'store/sheet_drawing.html', context)




from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required(login_url='login')
def save_cuts(request, sheet_id):
   
    if request.method == 'POST':
        try:
            sheet = product_qr.objects.get(id=sheet_id)
            cuts_json = request.POST.get("cuts")

            if not cuts_json:
                return JsonResponse({'status': 'error', 'message': 'No cuts data received'}, status=400)

            # Overwrite old cuts for the sheet (optional cleanup)
            
            try:
                
                instance = SheetCut.objects.get(sheet=sheet)
                instance. data=json.loads(cuts_json)
                instance.save()

            except SheetCut.DoesNotExist:  

                SheetCut.objects.create(
                    sheet=sheet,
                    data=json.loads(cuts_json)
                )

            return JsonResponse({'status': 'success'})
        except product_qr.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Sheet not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


@csrf_exempt
@login_required(login_url='login')
def get_cuts(request, sheet_id):
    try:
        sheet = product_qr.objects.get(id=sheet_id)
        cut = SheetCut.objects.filter(sheet=sheet).first()

        if cut:
            return JsonResponse({'cuts': cut.data})
        else:
            return JsonResponse({'cuts': None})
    except product_qr.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Sheet not found'}, status=404)