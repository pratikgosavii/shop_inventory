from email import message
from genericpath import samefile
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd


from store.views import numOfDays
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from functools import reduce

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




# Create your views here.

# @login_required(login_url='login')
# def add_inward(request):



#     godown_id = request.session.get('gowdown')
     
#     if godown_id == None:
#         godown_instance = godown.objects.first()
#         godown_id = godown_instance.id
#         request.session["gowdown"] = godown_id

#     else:

#         godown_instance = godown.objects.get(id = godown_id)



#     if request.method == 'POST':

#         forms = inward_Form(request.POST)
#         DC_date = request.POST.get('DC_date')


#         if DC_date:

#             date_time = DC_date
#         else:
#             date_time = datetime.now(IST)
#         updated_request = request.POST.copy()
#         updated_request.update({'DC_date': date_time})
#         forms = inward_Form(updated_request)

#         if forms.is_valid():
#             forms.save()

#             b = forms.cleaned_data['company_goods']
#             c = forms.cleaned_data['goods_company']
#             e = forms.cleaned_data['bags']
#             g = forms.cleaned_data['godown']

#             try:
#                 test = stock.objects.get(godown = g, company_goods = b, goods_company = c)

#                 test.total_bag = test.total_bag + e
#                 test.save()

#                 return redirect('add_inward')


#             except stock.DoesNotExist:

#                 test = stock.objects.create(godown = g, company_goods = b, goods_company = c, total_bag = e)
#                 godown_instance = godown.objects.get(id = godown_id)
#                 company_goods_data = company_goods.objects.filter(godown = godown_instance)

#                 context = {
#                     'form': forms,
#                     'godown_instance' : godown_instance,
#                     'company_goods_data' : company_goods_data


#                 }
               
#                 return render(request, 'transactions/add_inward.html', context)


#         else:

#             godown_instance = godown.objects.get(id = godown_id)
#             company_goods_data = company_goods.objects.filter(godown = godown_instance)

#             context = {
#                 'form': forms,
#                 'godown_instance' : godown_instance,
#                 'company_goods_data' : company_goods_data

#             }
            
#             return render(request, 'transactions/add_inward.html', context)



#     else:

#         forms = inward_Form()

#         godown_instance = godown.objects.get(id = godown_id)

#         company_goods_data = company_goods.objects.filter(godown = godown_instance)
             
#         context = {
#             'form': forms,
#             'godown_instance' : godown_instance,
#             'company_goods_data' : company_goods_data

#         }
        
#         return render(request, 'transactions/add_inward.html', context)


# @login_required(login_url='login')
# def update_inward(request, inward_id ):


#     if request.method == 'POST':

#         instance_inward = inward.objects.get(id = inward_id)


#         company_goods_id = request.POST.get('company_goods')
#         goods_company_id = request.POST.get('goods_company')
#         bags = request.POST.get('bags')

#         DC_date = request.POST.get('DC_date')

#         if DC_date:

#             date_time = DC_date

#         else:
#             date_time = datetime.now(IST)


#         updated_request = request.POST.copy()
#         updated_request.update({'DC_date': date_time})
#         forms = inward_Form(updated_request, instance=instance_inward)


#         if forms.is_valid():

#             instance_inward = inward.objects.get(id = inward_id)

#             if int(instance_inward.company_goods.id) != int(company_goods_id) or int(instance_inward.goods_company.id) != int(goods_company_id):

#                 try:

#                     company_goods_instance = company_goods.objects.get(id = company_goods_id) 
#                     goods_company_instance = goods_company.objects.get(id = goods_company_id) 

#                     test = stock.objects.get(company_goods = company_goods_instance, goods_company = goods_company_instance)
#                     test.total_bag = test.total_bag + int(bags)
#                     test.save()

#                 except stock.DoesNotExist:
#                     stock.objects.create(company_goods = company_goods_instance, goods_company = goods_company_instance, total_bag =  int(bags))


#                 company_goods_instance = company_goods.objects.get(id = instance_inward.company_goods.id)
#                 goods_company_instance = goods_company.objects.get(id = instance_inward.goods_company.id)

#                 stock_before = stock.objects.get(company_goods = company_goods_instance, goods_company = goods_company_instance)
#                 stock_before.total_bag = stock_before.total_bag - instance_inward.bags
#                 stock_before.save()

               
                    
               
                    
#                 forms.save()

#                 return HttpResponseRedirect(reverse('list_inward'))
            
#             else:

#                 minus_stock = None

#                 if instance_inward.bags != int(bags):

#                     test = stock.objects.get(company_goods = company_goods_id, goods_company = goods_company_id)

#                     if instance_inward.bags > int(bags):
#                         minus_stock = instance_inward.bags - int(bags)

#                     else:
#                         add_stock = int(bags) - instance_inward.bags

#                     if minus_stock:

#                         if test.total_bag >= minus_stock:

#                             test.total_bag = test.total_bag - minus_stock
#                             test.save()
#                             forms.save()
#                             return redirect('list_inward')

#                         else:
                        
#                             messages.error(request, "Outward is more than Stock")
#                             return redirect('list_inward')

#                     else:

#                         test.total_bag = test.total_bag + add_stock
#                         test.save()

#                         forms.save()

#                         return redirect('list_inward')

#                 else:

#                     forms.save()
#                     return HttpResponseRedirect(reverse('list_inward'))

#         else:
        
#             instance = inward.objects.get(id = inward_id)
#             company_goods_id = forms.instance.company_goods.id
#             category_id = forms.instance.goods_company.id
#             print('company_goods_id')
#             print(company_goods_id)
#             context = {
#                 'form': forms,
#                 'company_goods_ID' : company_goods_id,
#                 'category_ID' : category_id,
#             }
            

#             return render(request, 'transactions/update_inward.html', context)

            

        

#     else:

#         instance = inward.objects.get(id = inward_id)
#         forms = inward_Form(instance = instance)
#         company_goods_id = forms.instance.company_goods.id
#         category_id = forms.instance.goods_company.id
#         print('company_goods_id')
#         print(company_goods_id)
#         context = {
#             'form': forms,
#             'company_goods_ID' : company_goods_id,
#             'category_ID' : category_id,
#         }
#         return render(request, 'transactions/update_inward.html', context)


# @login_required(login_url='login')
# def delete_inward(request, inward_id):

#     try:
#         con = inward.objects.filter(id = inward_id).first()

#         test = stock.objects.get(godown = con.godown, company_goods = con.company_goods, goods_company = con.goods_company)
#         if test.total_bag >= con.bags:
#             test.total_bag = test.total_bag - con.bags
#             test.save()
#             con.delete()

#         else:

#             messages.error(request, 'cant delete stock is less')

#             return HttpResponseRedirect(reverse('list_inward_delete'))



#         return HttpResponseRedirect(reverse('list_inward_delete'))


#     except:
#         return HttpResponseRedirect(reverse('list_inward_delete'))




# @login_required(login_url='login')
# def list_inward(request):

#     year = request.GET.get('year')
#     godown_id = request.session['gowdown']

#     if godown_id == None:
#         godown_instance = godown.objects.first()
#         godown_id = godown_instance.id
#         request.session["gowdown"] = godown_id


#     if year:

#         date1 = str(int(year) - 1) + '-04-01'
#         date2 = year + '-03-31'
    
#         data = inward.objects.filter(DC_date__range=[date1, date2], godown__id = godown_id).order_by("-id")
    
#     else:

#         data = inward.objects.filter(godown__id = godown_id).order_by("-id")

#     outward_filter_data = outward_filter(request.GET, queryset = data)
    
#     data1 = []
#     data2 = []


#     data1.append('Godown')
#     data1.append('Category')
#     data1.append('Size')
#     data1.append('DC number')
#     data1.append('Quantity')
#     data1.append('Date')
#     data2.append(data1)


#     if outward_filter_data.qs:

#         for i in outward_filter_data.qs:

#             data1 = []

#             data1.append(i.godown.name)
#             data1.append(i.company_goods.name)
#             data1.append(i.goods_company.goods_company_name)
#             data1.append(i.DC_number)
#             data1.append(i.bags)
#             data1.append(i.DC_date) 

#             data2.append(data1)


#             data1 = []



#     time =  str(datetime.now(ist))
#     time = time.split('.')
#     time = time[0].replace(':', '-')

#     name = "Report.csv"
#     path = os.path.join(BASE_DIR) + '\static\csv\\' + name
#     with open(path,  'w', newline="") as f:
#         writer = csv.writer(f)
#         writer.writerows(data2)

#     link = os.path.join(BASE_DIR) + '\static\csv\\' + name

#     page = request.GET.get('page', 1)
#     paginator = Paginator(data, 50)

#     try:
#         data = paginator.page(page)
#     except PageNotAnInteger:
#         data = paginator.page(1)
#     except EmptyPage:
#         data = paginator.page(paginator.num_pages)
    
#     company_goods_data = company_goods.objects.filter(godown__id = godown_id)

#     context = {
#         'data': outward_filter_data.qs,
#         'year' : year,
#         'company_goods_data' : company_goods_data,
#         'outward_filter' : outward_filter(),
#         'link' : link,
        
#     }

#     return render(request, 'transactions/list_inward.html', context)


# import json

# @login_required(login_url='login')
# def add_outward(request):


#     godown_id = request.session.get('gowdown')
     
#     if godown_id == None:
#         godown_instance = godown.objects.first()
#         godown_id = godown_instance.id
#         request.session["gowdown"] = godown_id
    
#     else:
#         godown_instance = godown.objects.get(id = godown_id)


#     if request.method == 'POST':

#         forms = outward_Form(request.POST)
#         DC_date = request.POST.get('DC_date')


#         if DC_date:

#             date_time = DC_date
#         else:
#             date_time = datetime.now(IST)


#         updated_request = request.POST.copy()
#         updated_request.update({'DC_date': date_time})
#         forms = outward_Form(updated_request)

#         if forms.is_valid():

#             b = forms.cleaned_data['company_goods']
#             c = forms.cleaned_data['goods_company']
#             e = forms.cleaned_data['bags']
#             g = forms.cleaned_data['godown']

#             try:
#                 test = stock.objects.get(godown = g, company_goods = b, goods_company = c)

#                 if test.total_bag >= e:

#                     test.total_bag = test.total_bag - e
#                     test.save()
#                     forms.save()

                    
#                     return redirect('add_outward')


#                 else:
#                     print('I am here')
#                     messages.error(request, 'Outward is more than stock')
#                     godown_instance = godown.objects.get(id = godown_id)
#                     company_goods_data = company_goods.objects.filter(godown = godown_instance)
#                     print(company_goods_data)
#                     context = {
#                         'form': forms,
#                         'godown_instance': godown_instance,
#                         'company_goods_data': company_goods_data

#                     }
#                     return render(request, 'transactions/add_outward.html', context)



#             except stock.DoesNotExist:
               
#                 messages.error(request,"no stock in inverntory")
#                 godown_instance = godown.objects.get(id = godown_id)
#                 company_goods_data = company_goods.objects.filter(godown = godown_instance)

#                 context = {
#                     'form': forms,
#                     'godown_instance': godown_instance,
#                     'company_goods_data': company_goods_data

#                 }
               
#                 return render(request, 'transactions/add_outward.html', context)


#         else:

            
#             godown_instance = godown.objects.get(id = godown_id)
#             company_goods_data = company_goods.objects.filter(godown = godown_instance)


#             context = {
#                 'form': forms,
#                 'godown_instance': godown_instance,
#                 'company_goods_data': company_goods_data

#             }
#             return render(request, 'transactions/add_outward.html', context)




#     else:

#         forms = outward_Form()

#         godown_instance = godown.objects.get(id = godown_id)
#         company_goods_data = company_goods.objects.filter(godown = godown_instance)


#         context = {
#             'form': forms,
#             'godown_instance': godown_instance,
#             'company_goods_data': company_goods_data

#         }
#         return render(request, 'transactions/add_outward.html', context)


# @login_required(login_url='login')
# def report_dashbord(request):

#     inward_filter_data = inward_filter()
#     outward_filter_data = outward_filter()



#     context = {
#             'filter_inward': inward_filter_data,
#             'filter_outward': outward_filter_data,
#         }

#     return render(request, 'transactions/report_dashbord.html', context)



# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# @login_required(login_url='login')
# def list_outward(request):


#     year = request.GET.get('year')
#     godown_id = request.session['gowdown']

#     if godown_id == None:
#         godown_instance = godown.objects.first()
#         godown_id = godown_instance.id
#         request.session["gowdown"] = godown_id


#     if year:

#         date1 = str(int(year) - 1) + '-04-01'
#         date2 = year + '-03-31'

#         data = outward.objects.filter(DC_date__range=[date1, date2], godown__id = godown_id).order_by("-id")
    
#     else:

#         data = outward.objects.filter(godown__id = godown_id).order_by('-id')


#     outward_filter_data = outward_filter(request.GET, queryset = data)
    
#     data1 = []
#     data2 = []


#     data1.append('Godown')
#     data1.append('Category')
#     data1.append('Size')
#     data1.append('Dealer')
#     data1.append('DC number')
#     data1.append('Quantity')
#     data1.append('Employee name')
#     data1.append('Buyer name')
#     data1.append('Date')
#     data2.append(data1)


#     if outward_filter_data.qs:

#         for i in outward_filter_data.qs:

#             data1 = []

#             data1.append(i.godown.name)
#             data1.append(i.company_goods.name)
#             data1.append(i.goods_company.goods_company_name)
#             data1.append(i.dealer)
#             data1.append(i.DC_number)
#             data1.append(i.bags)
#             data1.append(i.employee_name) 
#             data1.append(i.gate_pass_name) 
#             data1.append(i.DC_date) 

#             data2.append(data1)


#             data1 = []



#     time =  str(datetime.now(ist))
#     time = time.split('.')
#     time = time[0].replace(':', '-')

#     name = "Report.csv"
#     path = os.path.join(BASE_DIR) + '\static\csv\\' + name
#     with open(path,  'w', newline="") as f:
#         writer = csv.writer(f)
#         writer.writerows(data2)

#     link = os.path.join(BASE_DIR) + '\static\csv\\' + name

#     agent_name = request.GET.get('agent_name')

#     if agent_name:

#         data = data.filter(agent__name__icontains=agent_name)

#     page = request.GET.get('page', 1)
#     paginator = Paginator(data, 50)
#     company_goods_data = company_goods.objects.filter(godown__id = godown_id)

#     try:
#         data = paginator.page(page)
#     except PageNotAnInteger:
#         data = paginator.page(1)
#     except EmptyPage:
#         data = paginator.page(paginator.num_pages)

#     context = {
#         'data': outward_filter_data.qs,
#         'year' : year,
#         'link' : link,
#         'company_goods_data' : company_goods_data,
#         'outward_filter' : outward_filter


#     }

#     return render(request, 'transactions/list_outward.html', context)

# @login_required(login_url='login')
# def update_outward(request, outward_id):


#     if request.method == 'POST':

#         instance = outward.objects.get(id = outward_id)
      
        
#         company_goods_id = request.POST.get('company_goods')
#         goods_company_id = request.POST.get('goods_company')

#         company_goods_instance = company_goods.objects.get(id = company_goods_id) 
#         goods_company_instance = goods_company.objects.get(id = goods_company_id) 

#         bags = request.POST.get('bags')

#         DC_date = request.POST.get('DC_date')

#         print(DC_date)

        

#         if DC_date:

#             date_time = DC_date

#         else:
#             date_time = datetime.now(IST)


#         updated_request = request.POST.copy()
#         updated_request.update({'DC_date': date_time})
#         forms = outward_Form(updated_request, instance=instance)

#         if forms.is_valid():

#             instance = outward.objects.get(id = outward_id)

#             try:
                
#                 if int(instance.company_goods.id) != int(company_goods_id) or int(instance.goods_company.id) != int(goods_company_id):


                    
#                     try:
                      
#                         test = stock.objects.get(company_goods = company_goods_instance, goods_company = goods_company_instance)
                      

#                     except stock.DoesNotExist:
#                         test = None
#                         stock.objects.create(company_goods = company_goods_instance, goods_company = goods_company_instance, total_bag =  int(bags))


#                     if test.total_bag >= int(bags):
                        
#                         test.total_bag = test.total_bag - int(bags)
#                         test.save()

#                         stock_before = stock.objects.get(company_goods = instance.company_goods.id, goods_company = instance.goods_company.id)
                        
#                         stock_before.total_bag = stock_before.total_bag + instance.bags
#                         stock_before.save()
#                         forms.save()

                     
#                         return redirect('list_outward')

#                     else:
#                         messages.error(request, "Outward is more than Stock")
#                         return redirect('list_outward')
                    
#                 else:

#                     if instance.bags != int(bags):
                        
#                         test = stock.objects.get(company_goods = company_goods_instance, goods_company = goods_company_instance)
                        
#                         add_stock = None
#                         minus_stock = None

#                         if instance.bags > int(bags):
#                             add_stock = instance.bags - int(bags)
#                         else:
#                             minus_stock = int(bags) - instance.bags

#                         if minus_stock:

#                             if test.total_bag >= minus_stock:

#                                 test.total_bag = test.total_bag - minus_stock
#                                 test.save()

#                                 forms.save()
#                             else:

#                                 messages.error(request, "Outward is more than Stock")
#                                 return redirect('list_outward')

                        
#                         else:

#                             test.total_bag = test.total_bag + add_stock
#                             test.save()

#                             forms.save()

#                         return redirect('list_outward')

#                     else:
#                         forms.save()
#                         return HttpResponseRedirect(reverse('list_outward'))

                    

#             except stock.DoesNotExist:

#                 messages.error(request, 'no stock in inventory for outward')
#                 return redirect('list_outward')

           

#         else:
           
#             comapny_goods_ID = forms.instance.company_goods.id
#             category_id = forms.instance.goods_company.id
          
#             context = {
#                 'form':  forms,
#                 'comapny_goods_ID' : comapny_goods_ID,
#                 'category_ID' : category_id,
#             }

#             return render(request, 'transactions/update_outward.html', context)



#     else:

#         instance = outward.objects.get(id = outward_id)
#         forms = outward_Form(instance = instance)
#         comapny_goods_ID = forms.instance.company_goods.id
#         category_id = forms.instance.goods_company.id
          
#         context = {
#             'form':  forms,
#             'comapny_goods_ID' : comapny_goods_ID,
#             'category_ID' : category_id,
#         }

#         return render(request, 'transactions/update_outward.html', context)


# @login_required(login_url='login')
# def delete_outward(request, outward_id):

#     a = stock.objects.all()

#     try:
#         con = outward.objects.get(id = outward_id)

#         test = stock.objects.get(godown = con.godown, company_goods = con.company_goods, goods_company = con.goods_company)
#         test.total_bag = test.total_bag + con.bags
#         test.save()
#         con.delete()

#         return HttpResponseRedirect(reverse('list_outward_delete'))


#     except Exception as e:
#         return HttpResponseRedirect(reverse('list_outward_delete'))


from .filters import *

@login_required(login_url='login')
def list_stock(request):

   
    data = stock.objects.prefetch_related('product__project_material_re').all()
   
    context = {
        'data': data,
        
    }

    return render(request, 'transactions/list_stock.html', context)

@login_required(login_url='login')
def list_left_over_stock(request):

   
    data = left_over_stock.objects.all()
   
    context = {
        'data': data,
        
    }

    return render(request, 'transactions/list_left_over_stock.html', context)

@login_required(login_url='login')
def list_dead_stock(request):

   
    data = scratch_stock.objects.all()
   
    context = {
        'data': data,
        
    }

    return render(request, 'transactions/list_dead_stock.html', context)


@login_required(login_url='login')
def report_inward(request):

    counteer = 1


    data = inward.objects.all().order_by("DC_number")

    filterd_data = inward_filter(request.GET, data)
    filtered_data = filterd_data.qs



    vals = []

    filterd_data = inward_filter(request.GET, data)
    filtered_data = filterd_data.qs
    # print(out)


    
    filtered_data = list(filtered_data.values_list('DC_number', 'company', 'company_goods__name', 'goods_company__goods_company_name', 'bags', 'DC_date'))

    vals1 = []
    vals1.append('Serial')
    vals1.append("DC Number")
    vals1.append("Company")
    vals1.append("Category")
    vals1.append("Size")
    vals1.append('Quantity')
    vals1.append('Date')

    vals.append(vals1)


    for i in filtered_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append(i[1])
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        vals1.append(i[5])

        vals.append(vals1)



       

    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')

    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    vals_list = vals
    vals_list.pop(0)


    print(vals_list)

    context = {
        'data': vals_list,
        'link' : link


    }

    return render(request, 'report/inward_report.html', context)



@login_required(login_url='login')
def report_outward(request):


    counteer = 1

   

    vals = []

    outward_data = outward.objects.all().order_by("DC_number")
    outward_filterd_data = outward_filter(request.GET, outward_data)
    outward_filterd_data = outward_filterd_data.qs

    outward_filterd_data = list(outward_filterd_data.values_list('DC_number', 'company', 'company_goods__name', 'goods_company__goods_company_name', 'dealer__bane', 'bags', 'DC_date'))
    # print(out)

    outward_filterd_data = list(map(list, outward_filterd_data))


    vals1 = []
    vals1.append('Serial')
    vals1.append("DC Number")
    vals1.append("Company")
    vals1.append("Category")
    vals1.append("Size")
    vals1.append("Dealer")
    vals1.append('Quantity')
    vals1.append('Date')
    vals.append(vals1)


    for i in outward_filterd_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append(i[1])
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        vals1.append(i[5])
        vals1.append(i[6])
        vals.append(vals1)

   

    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')

    print(vals)


    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)

    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    vals_list = vals
    vals_list.pop(0)


    context = {
        'data': vals_list,
        'link' : link


    }

    return render(request, 'report/outward_report.html', context)




@login_required(login_url='login')
def report_supply_return(request):

    data = supply_return.objects.all().order_by("DC_number")

    filterd_data = supply_return_filter(request.GET, data)
    data = filterd_data.qs

    vals = []


    filtered_data = list(data.values_list('DC_number', 'agent__name', 'agent__place', 'agent__taluka', 'agent__district', 'company_goods__name', 'goods_company__goods_company_name', 'bags', 'DC_date', 'transport__name', 'LR_number', 'freight'))


    vals1 = []
    vals1.append('Serial')
    vals1.append("DC Number")
    vals1.append("Party Name")
    vals1.append("Party Place")
    vals1.append("Party Taluka")
    vals1.append("Party District")
    vals1.append("Crop")
    vals1.append("Variety")
    vals1.append('Packet')
    vals1.append('Date')
    vals1.append('Transport')
    vals1.append('LR Number')
    vals1.append('Freight')
    vals.append(vals1)

    counteer = 1

    
    for i in filtered_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append(i[1])
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        vals1.append(i[5])
        vals1.append(i[6])
        vals1.append(i[7])
        vals1.append(i[8])
        vals1.append(i[9])
        vals1.append(i[10])
        vals1.append(i[11])
        vals.append(vals1)


    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')


    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)

    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    vals_list = vals
    vals_list.pop(0)


    context = {
        'data': vals_list,
        'link' : link,

    }

    return render(request, 'report/outward_report.html', context)


@login_required(login_url='login')
def generate_report_stock(request):

    godown_id = request.session.get('gowdown')
     
    if godown_id == None:
        godown_instance = godown.objects.first()
        godown_id = godown_instance.id
        request.session["gowdown"] = godown_id


    data_stock = stock.objects.filter(godown__id = godown_id).order_by('updated_at')

    stock_filter_data = stock_filter(request.GET, queryset = data_stock)
    
    data1 = []
    data2 = []


    data1.append('Godown')
    data1.append('Category')
    data1.append('Size')
    data1.append('Quantity')
    data2.append(data1)


    if stock_filter_data.qs:

        for i in stock_filter_data.qs:

            data1 = []

            data1.append(i.godown)
            data1.append(i.company_goods)
            data1.append(i.goods_company)
            data1.append(i.total_bag)

            data2.append(data1)

            data1 = []



    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')

    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data2)

    link = os.path.join(BASE_DIR) + '\static\csv\\' + name
    company_goods_data = company_goods.objects.filter(godown__id = godown_id)

    context = {
        'data': stock_filter_data.qs,
        'stock_filter_data' : stock_filter_data,
        'company_goods_data' : company_goods_data,
        'link' : link
    }

    return render(request, 'report/stock_report.html', context)


@login_required(login_url='login')
def generate_report_main(request):

    company_data = pd.DataFrame(list(company.objects.all().values('id', 'company_name')))
    company_data = dict(company_data.values)

    company_goods_data = pd.DataFrame(list(company_goods.objects.all().values('id', 'name')))
    company_goods_data = dict(company_goods_data.values)

    goods_company_data = pd.DataFrame(list(goods_company.objects.all().values('id', 'goods_company_name')))
    goods_company_data = dict(goods_company_data.values)

    agent_data = pd.DataFrame(list(agent.objects.all().values('id', 'name')))
    agent_data = dict(agent_data.values)
    
    agent_data2 = pd.DataFrame(list(agent.objects.all().values('id', 'name', 'place', 'taluka', 'district')))

    # return_data = supply_return.objects.all()

    outward_data = outward.objects.all()
    supply_return_data = supply_return.objects.all()
    outward_filterd_data = outward_filter(request.GET, outward_data)
    supply_return_filterd_data = outward_filter(request.GET, supply_return_data)

    if outward_data and not supply_return_data:
        
        # outward sum
        df2 = pd.DataFrame(list(outward_filterd_data.qs.values()))
        sum__ = df2.groupby(['company_id', 'company_goods_id', 'goods_company_id', 'agent_id']).sum().reset_index()

        sum__['bags_x'] = sum__['bags']
        sum__['bags_y'] = None
        sum__['bags_z'] = sum__['bags']
        sum__['company_id'] = sum__['company_id'].map(company_data)
        sum__['company_goods_id'] = sum__['company_goods_id'].map(company_goods_data)
        sum__['goods_company_id'] = sum__['goods_company_id'].map(goods_company_data)
        sum__['agent_id'] = sum__['agent_id'].map(agent_data)
        

        out = (sum__.merge(agent_data2, left_on='agent_id', right_on='name').reindex(columns=['agent_id', 'place', 'taluka', 'district', 'company_id', 'company_goods_id', 'goods_company_id', 'bags_x', 'bags_y', 'bags_z']))



    elif supply_return_data and not outward_data:
        #return sum
        df3 = pd.DataFrame(list(supply_return_filterd_data.qs.values()))

        sum__2 = df3.groupby(['company_id', 'company_goods_id', 'goods_company_id', 'agent_id']).sum().reset_index()

        sum__2['bags_x'] = None
        sum__2['bags_y'] = sum__2['bags']
        sum__2['bags_z'] = sum__2['bags']
        sum__2['company_id'] = sum__2['company_id'].map(company_data)
        sum__2['company_goods_id'] = sum__2['company_goods_id'].map(company_goods_data)
        sum__2['goods_company_id'] = sum__2['goods_company_id'].map(goods_company_data)
        sum__2['agent_id'] = sum__2['agent_id'].map(agent_data)
        

        out = (sum__2.merge(agent_data2, left_on='agent_id', right_on='name').reindex(columns=['agent_id', 'place', 'taluka', 'district', 'company_id', 'company_goods_id', 'goods_company_id', 'bags_x', 'bags_y', 'bags_z']))




    else:

        df2 = pd.DataFrame(list(outward_filterd_data.qs.values()))

        df3 = pd.DataFrame(list(supply_return_filterd_data.qs.values()))


        sum__ = df2.groupby(['company_id', 'company_goods_id', 'goods_company_id', 'agent_id']).sum().reset_index()
        sum__2 = df3.groupby(['company_id', 'company_goods_id', 'goods_company_id', 'agent_id']).sum().reset_index()


        final_ou = pd.merge(sum__, sum__2, on=['company_id', 'company_goods_id', 'goods_company_id', 'agent_id'], how="outer")[['company_id', 'company_goods_id', 'goods_company_id', 'agent_id', 'bags_x', 'bags_y']]
        final_ou['bags_z'] = final_ou.fillna(0)['bags_x'] - final_ou.fillna(0)['bags_y']

        
        final_ou['company_id'] = final_ou['company_id'].map(company_data)
        final_ou['company_goods_id'] = final_ou['company_goods_id'].map(company_goods_data)
        final_ou['goods_company_id'] = final_ou['goods_company_id'].map(goods_company_data)
        final_ou['agent_id'] = final_ou['agent_id'].map(agent_data)

        out = (final_ou.merge(agent_data2, left_on='agent_id', right_on='name').reindex(columns=['company_id', 'agent_id', 'place', 'taluka', 'district', 'company_goods_id', 'goods_company_id', 'bags_x', 'bags_y', 'bags_z']))

        print(out)

        # print(out)

    vals = out.values

    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')
        


    
    vals_list = (vals.tolist())
    vals1 = []
    vals1.append("Party Name")
    vals1.append("Party Place")
    vals1.append("Party Taluka")
    vals1.append("Party District")
    vals1.append("Company")
    vals1.append("Crop")
    vals1.append("Variety")
    vals1.append('Supply Packet')
    vals1.append('Return Packet')
    vals1.append('Net Packet')

    vals_list.insert(0, vals1)

    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')


    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals_list)


    link = os.path.join(BASE_DIR) + '\static\csv\\' + name


    outward_filter_data = outward_filter()

    vals_list = (vals.tolist())

    company_data = company.objects.all()

    context = {
        'data' : vals_list,
        'filter_outward' : outward_filter_data,
        'link' : link,
        'company_data' : company_data

    }

    return render(request, 'report/main_report.html', context)
    

@login_required(login_url='login')
def generate_report_daily(request):

    pd.set_option('display.float_format', '{:.2f}'.format)

    #DC_date_start__date=2022-02-28&DC_date_end__date=2022-02-28

    company_data = pd.DataFrame(list(company.objects.all().values('id', 'company_name')))
    company_data = dict(company_data.values)

    company_goods_data = pd.DataFrame(list(company_goods.objects.all().values('id', 'name')))
    company_goods_data = dict(company_goods_data.values)

    goods_company_data = pd.DataFrame(list(goods_company.objects.all().values('id', 'goods_company_name')))
    goods_company_data = dict(goods_company_data.values)

    inward_data = inward.objects.filter(DC_date = datetime.now())
    outward_data = outward.objects.filter(DC_date = datetime.now())
    supply_return_data = outward.objects.filter(DC_date = datetime.now())
    inward_filterd_data = inward_filter(request.GET, inward_data)
    outward_data_filterd_data = outward_filter(request.GET, outward_data)
    if inward_data:
        # inward sum
        df = pd.DataFrame(list(inward_filterd_data.qs.values()))
        sum__ = df.groupby(['company_id', 'company_goods_id', 'goods_company_id']).sum().reset_index()
    else:
        sum__ = pd.DataFrame(columns=['company_id', 'company_goods_id', 'goods_company_id', 'id', 'agent_id', 'bags', 'DC_number'])

    if outward_data:
        # outward sum
        df2 = pd.DataFrame(list(outward_data_filterd_data.qs.values()))
        sum__2 = df2.groupby(['company_id', 'company_goods_id', 'goods_company_id']).sum().reset_index()
        
    else:
        sum__2 = pd.DataFrame(columns=['company_id', 'company_goods_id', 'goods_company_id', 'id', 'agent_id', 'bags', 'DC_number'])

    if supply_return_data:
        
        #return sum
        df3 = pd.DataFrame(list(supply_return_data.values()))
        sum__3 = df3.groupby(['company_id', 'company_goods_id', 'goods_company_id']).sum().reset_index()

    else:
        sum__3 = pd.DataFrame(columns=['company_id', 'company_goods_id', 'goods_company_id', 'id', 'agent_id', 'bags', 'DC_number'])

    #stock
    sum__4 = pd.DataFrame(list(stock.objects.all().values()))

    data_frames = [sum__, sum__2, sum__3, sum__4]

    ada = reduce(lambda  left,right: pd.merge(left,right,on=['company_id', 'company_goods_id', 'goods_company_id'], how='outer'), data_frames)[['company_id', 'company_goods_id', 'goods_company_id', 'bags_x', 'bags_y', 'bags', 'total_bag']]
    print('final')

   

    # m = pd.merge(sum__, sum__2, on=['company_id', 'company_goods_id', 'goods_company_id'], how="outer")[['company_id', 'company_goods_id', 'goods_company_id',  'bags_x', 'bags_y']]
    
    # print('m')
    # print(m)
    # m1 = pd.merge(m, sum__3, on=['company_id', 'company_goods_id', 'goods_company_id'], how="outer")[['company_id', 'company_goods_id', 'goods_company_id',  'bags_x', 'bags_y', 'bags']]
   
    # print('m1')
    # print(m1)
    # m2 = pd.merge(m1, sum__4, on=['company_id', 'company_goods_id', 'goods_company_id'], how="outer")[['company_id', 'company_goods_id', 'goods_company_id',  'bags_x', 'bags_y', 'bags', 'total_bag']]

    # print('m2')
    # print(m2)

    final_out = ada

    final_out['company_id'] = final_out['company_id'].map(company_data)
    final_out['company_goods_id'] = final_out['company_goods_id'].map(company_goods_data)
    final_out['goods_company_id'] = final_out['goods_company_id'].map(goods_company_data)

    vals = final_out.values
    
    time =  str(datetime.now(ist))
    time = time.split('.')
    time = time[0].replace(':', '-')

    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)

    outward_filter_data = outward_filter()

    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    vals_list = (vals.tolist())


    context = {
        'data': vals_list,
        'filter_outward' : outward_filter_data,
        'link' : link

    }

    return render(request, 'report/daily_report.html', context)




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






from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pdf_status = pisa.CreatePDF(html, dest=response)

    if pdf_status.err:
        return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

    return response


def ResultList(request, outward_id):
    template_name = "transactions/gate_pass.html"
    records = outward.objects.get(id = outward_id)

    return render_to_pdf(
        template_name,
        {
            "record": records,
        },
    )





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

  
    data = project.objects.all()

    
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






from store.forms import *

@login_required(login_url='login')
def add_project(request):


    if request.method == 'POST':

        print(request.POST)

        forms = project_Form(request.POST)
        


        category_id = request.POST.getlist("category")
        size_id = request.POST.getlist("size")
        thickness_id = request.POST.getlist("thickness")
        grade_id = request.POST.getlist("grade")
        quantity = request.POST.getlist("quantity")


        print(category_id)
        print(size_id)
        print(thickness_id )
        print(grade_id )
        print(quantity )


        if forms.is_valid():

            project_instance = forms.save()

            
            for a, b, c, d, i in zip(category_id, size_id, grade_id, thickness_id ,quantity):

                try:

                    obj, created = product.objects.get_or_create(category_id = a, size_id = b, grade_id = c, thickness_id = d)
                    product_id = obj

                except product.DoesNotExist:

                    product_id = created

                project_material_instance = project_material.objects.create(product = product_id, project = project_instance, quantity = i)

                for z in range(int(i)): 
                    project_matarial_qr.objects.create(project_material = project_material_instance)
              
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

        data_form = product_Form()

        context = {
            'form': forms,
            'data_form': data_form,
        }
        return render(request, 'transactions/add_project.html', context)

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


def show_scanner_assign_matarial_qr(request):

    return render(request, 'transactions/update_qr_scanner.html')




def update_assign_matarial_qr(request, product_qr_id):

    product_qr_instance = product_qr.objects.get(id = product_qr_id)

    if request.method == "POST":

        a = request.POST.get('size')
        b = request.POST.get('used_size')
        c = request.POST.get('left_size')
        e = request.POST.get('move_to_scratch')

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


        # Now, retrieve the related project_qr instance
    
        material_history.objects.create(product_qr = product_qr_instance, previous_size = size_instance1, used_size = size_instance2, left_size = size_instance3)
            
        if e == "true":

            print(' in scratch ')

            instance, created = scratch_stock.objects.get_or_create(product = product_instance)

            if product_qr_instance.moved_to_left_over != True:
            
                stock_instance = stock.objects.get(product = product_instance)
                stock_instance.quantity = stock_instance.quantity - 1
                
                product_qr_instance.moved_to_scratch = True
                product_qr_instance.save()

                stock_instance.save()

            else:
                
                left_over_instance =  left_over_stock.objects.get(product = product_instance)


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
                
                instance, created = left_over_stock.objects.get_or_create(product = product_instance)
            
                stock_instance, stock_created = stock.objects.get_or_create(product = product_instance)
                if stock_instance:
                    stock_instance.quantity = stock_instance.quantity - 1
                    stock_instance.save()
                else:
                    stock_created.quantity = 1
                    stock_created.save()

                product_qr_instance.moved_to_left_over = True
                product_qr_instance.save()

                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.product_qr = product_qr_instance
                    instance.save()

                else:

                    created.quantity = 1
                    created.save()
        print('-------------------')
        print('-------------------')
        print('-------------------')
        print(product_instance.category)
        print(product_instance.thickness)
        print(product_instance.grade)
        print(product_instance.shelf)
        print(size_instance3.id)
        print('-------------------')
        print('-------------------')
        print('-------------------')
        product_instance, product_created = product.objects.get_or_create(category = product_instance.category, thickness = product_instance.thickness, size = size_instance3, grade = product_instance.grade, shelf = product_instance.shelf)
        
        print('---------8888888888888888888888888888888888----------')
      
        
        if product_instance == None:
            product_qr_instance.product = product_created
        else:
            product_qr_instance.product = product_instance


        print(product_instance)
        print(product_instance.size)
            
        product_qr_instance.save()

        
        # remove project for this qr
        return JsonResponse({'status' : 'done'})


    else:

      
        context = {
            'data': product_qr_instance,
            'product_qr_id' : product_qr_id
        }

        return render(request, 'transactions/update_assign_material_qr.html', context)

    
from django.forms import modelformset_factory

def add_production(request, project_id):

    project_instance = project.objects.get(id = project_id)

    if request.method == "POST":

        quantity = request.POST.getlist('quantity[]')
        item_code_id = request.POST.getlist('item_code[]')
        material = request.POST.getlist('materialsId[]')


        for a,b,c in zip(material, item_code_id, quantity):

            instance = project_matarial_qr.objects.get(id = a)
            item_code_instance = item_code.objects.get(id = b)
            instance.item_code = item_code_instance
            instance.production_quantity = c
            instance.save()
       
        return JsonResponse({'status' : 'sdsd'})
        
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







import qrcode

from django.core.files.base import ContentFile
from io import BytesIO

from PIL import Image

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

        # Adjust the box_size based on the desired size
        box_size = qr_size // 4  # You can experiment with different values

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=4,
        )
        qr.add_data(a.id)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white", size=(qr_size, qr_size))
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        qr_code_image = ContentFile(buffer.getvalue())

        a.qr_code.save(f"qr_code_{a.id}.png", qr_code_image)

        qr_codes.append(img)

    pdf_data = generate_qr_codes_pdf(qr_codes)

    response = HttpResponse(pdf_data.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="qr_codes.pdf"'

    return response

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image


def print_single_qr(request, product_qr_id):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="images.pdf"'

    pdf_buffer = response
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    elements = []

    product_qr_instance = product_qr.objects.get(id = product_qr_id)
    image_path = product_qr_instance.qr_code.path

    # Adjust image size as needed
    image = Image(image_path, width=30, height=30)

    # Add a border and adjust the box size
    image.drawHeight = 200  # Set image height
    image.drawWidth = 300   # Set image width
    image.boxSize = [image.drawWidth + 20, image.drawHeight + 20]  # Adjust box size
    image.borderSize = 4    # Set border size
    image.borderColor = colors.black  # Set border color

    elements.append(image)

    doc.build(elements)

    return response

def list_generated_product_qr(request):

    data = product_qr.objects.all()

    context = {
        
        'data': data,
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
    

def assign_values_to_qr(request, product_qr_id):
    

    print('hereeeeeeee')
    product_id = product_qr_id

    
    product_qr_instance = product_qr.objects.get(id = product_id)

    if request.method == 'POST':

        form = product_Form(request.POST)

        if form.is_valid():
            book, created = product.objects.get_or_create(**form.cleaned_data)

            product_qr_instance.date_of_pur = request.POST.get('date_of_pur')
            product_qr_instance.save()

            if book:

                product_instance = book

            else:

                product_instance = created

            messages.success(request, 'values added successfully')

            instance, created = stock.objects.get_or_create(product = product_instance)

            if product_qr_instance.is_fix:

                instance_previous_stock = stock.objects.get(product = product_qr_instance.product)
                instance_previous_stock.quantity = instance_previous_stock.quantity - 1
                instance_previous_stock.save()
                
                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.save()

                else:

                    created.quantity = 1
                    created.save()

            else:

                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.save()

                else:

                    created.quantity = 1
                    created.save()
            
            product_qr_instance.product = product_instance
            product_qr_instance.is_fix = True
            product_qr_instance.save()

            redirect_url = reverse('assign_values_to_qr', args=[product_qr_id])

            return redirect(redirect_url)


    else:    

        form = product_Form(instance=product_qr_instance.product)
        form_qr = product_qr_Form(instance=product_qr_instance)

        print(product_qr_id)
        data = material_history.objects.filter(product_qr__id = product_qr_id)

         
        
        context = {
            'form': form,
            'form_qr': form_qr,
            'data': data,
            'product_qr_id': product_qr_id,
        }

        return render(request, 'transactions/assign_value_to_qr.html', context)
    


def assign_values_to_qr_page(request):

    scanned_value = request.POST.get("scanned_value")


    redirect_url = reverse('assign_values_to_qr', args=[scanned_value]) 
    response_data = {'status' : 'success', 'redirect_url': redirect_url}
    return JsonResponse(response_data)


def update_product(request, product_id):

    pass


    