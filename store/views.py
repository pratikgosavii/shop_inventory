from django.shortcuts import render, redirect
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
def get_company_goods_ajax(request):

    data = []
    

    if request.method == "POST":
        company_id = request.POST['company_id']
        try:
            instance = company.objects.filter(id = company_id).first()
            dropdown1 = company_goods.objects.filter(company = instance)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(dropdown1.values('id', 'name')), safe = False) 


@login_required(login_url='login')
def get_goods_company_ajax(request):

    data = []

    if request.method == "POST":
        company_id = request.POST['company_id']
        company_goods_id = request.POST['company_goods']
        try:
            company_instance = company.objects.get(id= company_id)
            instance = company_goods.objects.filter(id = company_goods_id).first()
            dropdown1 = goods_company.objects.filter(company_goods = instance, company_name= company_instance)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(dropdown1.values('id', 'goods_company_name')), safe = False) 


@login_required(login_url='login')
def get_agent_company_ajax(request):

    data = []
    print('i am here2')

    if request.method == "POST":
        company_id = request.POST['company_id']
        print(company_id)
        try:
            company_instance = company.objects.get(id= company_id)
            print(company_instance)
            
            agent_data = agent.objects.filter(company = company_instance)
            print(agent_data)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(agent_data.values('id', 'name')), safe = False) 


@login_required(login_url='login')
def get_category_ajax(request):

    data = []
    print('i am here2')

    if request.method == "POST":
        company_goods_id = request.POST['company_goods_id']
        print(company_goods_id)
        try:
            company_goods_instance = goods_company.objects.filter(category__id = company_goods_id)
            print(company_goods_instance)
            
         
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(company_goods_instance.values('id', 'goods_company_name')), safe = False) 



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

        instance = godown.objects.get(id=godown_id)

        forms = godown_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_godown')
        else:
            print(forms.errors)
    
    else:

        instance = godown.objects.get(id=godown_id)
        forms = godown_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_godown.html', context)

        

@login_required(login_url='login')
def delete_godown(request, godown_id):

    godown.objects.get(id=godown_id).delete()

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
def list_godown(request):

    data = godown.objects.all()

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



# @login_required(login_url='login')
# def add_company(request):

#     if request.method == 'POST':

#         forms = company_Form(request.POST)

#         if forms.is_valid():
#             forms.save()
#             return redirect('list_company')
#         else:
#             print(forms.errors)
    
#     else:

#         forms = company_Form()

#         context = {
#             'form': forms
#         }
#         return render(request, 'store/add_company.html', context)

        

# @login_required(login_url='login')
# def update_company(request, company_id):

#     if request.method == 'POST':

#         instance = company.objects.get(id=company_id)

#         forms = company_Form(request.POST, instance=instance)

#         if forms.is_valid():
#             forms.save()
#             return redirect('list_company')
#         else:
#             print(forms.errors)
    
#     else:

#         instance = company.objects.get(id=company_id)
#         forms = company_Form(instance=instance)

#         context = {
#             'form': forms
#         }
#         return render(request, 'store/add_company.html', context)

        

# @login_required(login_url='login')
# def delete_company(request, company_id):

#     company.objects.get(id=company_id).delete()

#     return HttpResponseRedirect(reverse('list_company_delete'))


        

# @login_required(login_url='login')
# def list_company(request):

#     data = company.objects.all()

#     context = {
#         'data': data
#     }

#     return render(request, 'store/list_company.html', context)



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
def update_size(request, company_goods_id):

    if request.method == 'POST':

        instance = size.objects.get(id=company_goods_id)

        forms = size_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_size')
    
    else:

        instance = size.objects.get(id=company_goods_id)

        

        forms = size_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_size.html', context)


@login_required(login_url='login')
def delete_size(request, company_goods_id):
    
    size.objects.get(id=company_goods_id).delete()

    return HttpResponseRedirect(reverse('list_size'))


@login_required(login_url='login')
def list_size(request):
    
     
    data = size.objects.all().order_by('name')

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
def update_thickness(request, company_goods_id):

    if request.method == 'POST':

        instance = thickness.objects.get(id=company_goods_id)

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

     

@login_required(login_url='login')
def list_company_delete(request):

    data = company.objects.all()

    context = {
        'data': data
    }

    return render(request, 'delete/list_company_delete.html', context)


@login_required(login_url='login')
def list_company_delete(request):

    data = company.objects.all()

    context = {
        'data': data
    }

    return render(request, 'delete/list_company_delete.html', context)



@login_required(login_url='login')
def list_godown_delete(request):
    
    data = godown.objects.all()
    context = {
            'data': data
        }


    return render(request, 'delete/list_godown_delete.html', context)

@login_required(login_url='login')
def list_company_goods_delete(request):
    
    data = company_goods.objects.all()
    context = {
            'data': data
        }


    return render(request, 'delete/list_company_goods_delete.html', context)



@login_required(login_url='login')
def list_goods_company_delete(request):
    
    data = goods_company.objects.all()

    context = {
            'data': data
        }


    return render(request, 'delete/list_goods_company_delete.html', context)




@login_required(login_url='login')
def list_agent_delete(request):
    
    data = agent.objects.all()

    context = {
            'data': data
        }


    return render(request, 'delete/list_agent_delete.html', context)


@login_required(login_url='login')
def list_transport_delete(request):
    
    data = transport.objects.all()

    context = {
            'data': data
        }


    return render(request, 'delete/list_transport_delete.html', context)

