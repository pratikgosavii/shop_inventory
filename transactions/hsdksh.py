from email import message
from genericpath import samefile
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

from store.views import numOfDays
from transactions.filters import inward_filter, outward_filter, stock_filter, supply_return_filter
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage
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




# Create your views here.

@login_required(login_url='login')
def add_inward(request):


    if request.method == 'POST':

        forms = inward_Form(request.POST)
        DC_date = request.POST.get('DC_date')


        if DC_date:

            date_time = numOfDays(DC_date)
            print('in if')
        else:
            date_time = datetime.now(IST)
        print('-----------------------------------------------date_time')
        print(date_time)
        print('---------------------')
        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time})
        forms = inward_Form(updated_request)

        if forms.is_valid():
            forms.save()

            a = forms.cleaned_data['company']
            b = forms.cleaned_data['company_goods']
            c = forms.cleaned_data['goods_company']
            d = forms.cleaned_data['agent']
            e = forms.cleaned_data['bags']

            try:
                test = stock.objects.get(company = a, company_goods = b, goods_company = c)

                test.total_bag = test.total_bag + e
                test.save()

                return redirect('list_inward')

            except stock.DoesNotExist:

                test = stock.objects.create(company = a, company_goods = b, goods_company = c, total_bag = e)
                return redirect('list_inward')
        else:
            print(forms.errors)

            form = inward_Form()
            context = {
                'form_error': forms.errors
            }
            return render(request, 'transactions/add_inward.html', context)

    else:

        forms = inward_Form()

        context = {
            'form': forms
        }
        return render(request, 'transactions/add_inward.html', context)


@login_required(login_url='login')
def update_inward(request, inward_id ):


    if request.method == 'POST':

        instance_inward = inward.objects.get(id = inward_id)

        data_inward = instance_inward

        company_id = request.POST.get('company')
        company_goods_id = request.POST.get('company_goods')
        goods_company_id = request.POST.get('goods_company')
        bags = request.POST.get('bags')

        DC_date = request.POST.get('DC_date')

        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)


        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time})
        forms = inward_Form(updated_request, instance=instance_inward)


        if forms.is_valid():

            instance_inward = inward.objects.get(id = inward_id)

            if int(instance_inward.company.id) != int(company_id) or int(instance_inward.company_goods.id) != int(company_goods_id) or int(instance_inward.goods_company.id) != int(goods_company_id):

                try:

                    company_instance = company.objects.get(id = company_id) 
                    company_goods_instance = company_goods.objects.get(id = company_goods_id) 
                    goods_company_instance = goods_company.objects.get(id = goods_company_id) 

                    test = stock.objects.get(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance)
                    test.total_bag = test.total_bag + int(bags)
                    test.save()

                    print('1')

                except stock.DoesNotExist:
                    stock.objects.create(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance, total_bag =  int(bags))


                company_instance = company.objects.get(id =instance_inward.company.id)
                company_goods_instance = company_goods.objects.get(id = instance_inward.company_goods.id)
                goods_company_instance = goods_company.objects.get(id = instance_inward.goods_company.id)

                stock_before = stock.objects.get(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance)
                stock_before.total_bag = stock_before.total_bag - instance_inward.bags
                stock_before.save()

               
                    
               
                    
                forms.save()

                return HttpResponseRedirect(reverse('list_inward'))
            
            else:

                minus_stock = None

                if instance_inward.bags != int(bags):

                    test = stock.objects.get(company = company_id, company_goods = company_goods_id, goods_company = goods_company_id)

                    if instance_inward.bags > int(bags):
                        minus_stock = instance_inward.bags - int(bags)

                    else:
                        add_stock = int(bags) - instance_inward.bags

                    if minus_stock:

                        if test.total_bag >= minus_stock:

                            test.total_bag = test.total_bag - minus_stock
                            test.save()
                            forms.save()
                            return redirect('list_inward')

                        else:
                        
                            messages.error(request, "Outward is more than Stock")
                            return redirect('list_inward')

                    else:

                        print(data_inward.bags)

                        test.total_bag = test.total_bag + add_stock
                        test.save()

                        forms.save()

                        return redirect('list_inward')

                else:

                    forms.save()
                    return HttpResponseRedirect(reverse('list_inward'))



            

        

    else:

        instance = inward.objects.get(id = inward_id)
        forms = inward_Form(instance = instance)
        comapnyID = forms.instance.company.id
        comapny_goods_ID = forms.instance.company_goods.id
        goods_company_ID = forms.instance.goods_company.id
        agent_ID = forms.instance.agent.id

        context = {
            'form': forms,
            'comapnyID' : comapnyID,
            'comapny_goods_ID' : comapny_goods_ID,
            'goods_company_ID' : goods_company_ID,
            'agent_ID' : agent_ID
        }
        return render(request, 'transactions/update_inward.html', context)


@login_required(login_url='login')
def delete_inward(request, inward_id):

    try:
        con = inward.objects.filter(id = inward_id).first()

        test = stock.objects.get(company = con.company, company_goods = con.company_goods, goods_company = con.goods_company)
        test.total_bag = test.total_bag - con.bags
        test.save()
        con.delete()

        return HttpResponseRedirect(reverse('list_inward_delete'))


    except:
        print('something went wrong')
        return HttpResponseRedirect(reverse('list_inward_delete'))




@login_required(login_url='login')
def list_inward(request):

    data = inward.objects.all()

    inward_filter_data = inward_filter()

    company_data = company.objects.all()

    context = {
        'data': data,
        'company_data' : company_data,
        'filter_inward' : inward_filter_data
    }

    return render(request, 'transactions/list_inward.html', context)


@login_required(login_url='login')
def add_outward(request):

    if request.method == 'POST':

        forms = outward_Form(request.POST)
        DC_date = request.POST.get('DC_date')

        date_time = numOfDays(DC_date)

        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)


        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time})
        forms = outward_Form(updated_request)

        print(DC_date)



        if forms.is_valid():

            a = forms.cleaned_data['company']
            b = forms.cleaned_data['company_goods']
            c = forms.cleaned_data['goods_company']
            e = forms.cleaned_data['bags']

            try:
                test = stock.objects.get(company = a, company_goods = b, goods_company = c)

                if test.total_bag >= e:

                    test.total_bag = test.total_bag - e
                    test.save()
                    print('save')
                    forms.save()

                    return redirect('list_outward')

                else:
                    messages.error(request, "Outward is more than Stock")
                    print('Outward is more than Stock')
                    return redirect('list_outward')


            except stock.DoesNotExist:

                messages.error(request, 'no stock in inventory for outward')
                return redirect('list_outward')


        else:
            print(forms.errors)

    else:

        forms = outward_Form()

        context = {
            'form': forms
        }
        return render(request, 'transactions/add_outward.html', context)


@login_required(login_url='login')
def report_dashbord(request):

    inward_filter_data = inward_filter()
    outward_filter_data = outward_filter()



    context = {
            'filter_inward': inward_filter_data,
            'filter_outward': outward_filter_data,
        }

    return render(request, 'transactions/report_dashbord.html', context)



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='login')
def list_outward(request):

    data = outward.objects.filter().order_by('DC_number')


    agent_name = request.GET.get('agent_name')

    if agent_name:

        data = data.filter(agent__name__icontains=agent_name)

    

    outward_filter_data = outward_filter()

    company_data = company.objects.all()



    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    print(data)


    context = {
        'data': data,
        'filter_outward' : outward_filter_data,
        'company_data' : company_data
    }

    return render(request, 'transactions/list_outward.html', context)

@login_required(login_url='login')
def update_outward(request, outward_id):


    if request.method == 'POST':

        instance = outward.objects.get(id = outward_id)
        print('before')
        print(instance.goods_company)
       
        
        company_id = request.POST.get('company')
        company_goods_id = request.POST.get('company_goods')
        goods_company_id = request.POST.get('goods_company')

        company_instance = company.objects.get(id = company_id) 
        company_goods_instance = company_goods.objects.get(id = company_goods_id) 
        goods_company_instance = goods_company.objects.get(id = goods_company_id) 

        bags = request.POST.get('bags')

        DC_date = request.POST.get('DC_date')

        date_time = numOfDays(DC_date)

        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)


        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time})
        forms = outward_Form(updated_request, instance=instance)

        print('2')

        if forms.is_valid():

            print('3')

            instance = outward.objects.get(id = outward_id)

            try:

                print('testing ------------------------')

                
                if int(instance.company.id) != int(company_id) or int(instance.company_goods.id) != int(company_goods_id) or int(instance.goods_company.id) != int(goods_company_id):


                    
                    try:
                        test = stock.objects.get(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance)

                        test = stock.objects.get(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance)
                        test.total_bag = test.total_bag - int(bags)
                        test.save()

                    except stock.DoesNotExist:
                        stock.objects.create(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance, total_bag =  int(bags))


                    if test.total_bag >= int(bags):
                        
                        print('entered bags')
                        
                        print(test.total_bag, bags)
                        test.total_bag = test.total_bag - int(bags)
                        test.save()

                        stock_before = stock.objects.get(company = instance.company.id, company_goods = instance.company_goods.id, goods_company = instance.goods_company.id)
                        
                        stock_before.total_bag = stock_before.total_bag + instance.bags
                        stock_before.save()
                        forms.save()

                        return redirect('list_outward')

                    else:
                        messages.error(request, "Outward is more than1 Stock")
                        print('Outward is more than Stock')
                        return redirect('list_outward')
                    
                    
                else:

                    print('wored')

                    if instance.bags != int(bags):
                        
                        test = stock.objects.get(company = company_instance, company_goods = company_goods_instance, goods_company = goods_company_instance)
                        
                        add_stock = None
                        minus_stock = None

                        if instance.bags > int(bags):
                            add_stock = instance.bags - int(bags)
                        else:
                            minus_stock = int(bags) - instance.bags

                        if minus_stock:

                            if test.total_bag >= minus_stock:

                                test.total_bag = test.total_bag - minus_stock
                                test.save()
                                print('save')

                                forms.save()
                            else:

                                messages.error(request, "Outward is more than Stock")
                                print('Outward is more than Stock')
                                return redirect('list_outward')

                        
                        else:

                            test.total_bag = test.total_bag + add_stock
                            test.save()
                            print('save')

                            forms.save()

                        return redirect('list_outward')

                    else:
                        forms.save()
                        return HttpResponseRedirect(reverse('list_outward'))

                    

            except stock.DoesNotExist:

                messages.error(request, 'no stock in inventory for outward')
                return redirect('list_outward')

           

        else:
           
            print(forms.errors)

    else:

        instance = outward.objects.get(id = outward_id)
        forms = outward_Form(instance = instance)
        comapnyID = forms.instance.company.id
        comapny_goods_ID = forms.instance.company_goods.id
        goods_company_ID = forms.instance.goods_company.id
        agent_ID = forms.instance.agent.id

        context = {
            'form': forms,
            'comapnyID' : comapnyID,
            'comapny_goods_ID' : comapny_goods_ID,
            'goods_company_ID' : goods_company_ID,
            'agent_ID' : agent_ID
        }
        return render(request, 'transactions/update_outward.html', context)


@login_required(login_url='login')
def delete_outward(request, outward_id):

    try:
        con = outward.objects.get(id = outward_id)

        test = stock.objects.get(company = con.company, company_goods = con.company_goods, goods_company = con.goods_company)
        test.total_bag = test.total_bag + con.bags
        test.save()
        con.delete()

        return HttpResponseRedirect(reverse('list_outward_delete'))


    except:
        print('something went wrong')
        return HttpResponseRedirect(reverse('list_outward_delete'))


@login_required(login_url='login')
def list_stock(request):

    data = stock.objects.all()

    stock_filter_data = stock_filter()

    company_data = company.objects.all()

    context = {
        'data': data,
        'stock_filter' : stock_filter_data,
        'company_data': company_data
    }

    return render(request, 'transactions/list_stock.html', context)


@login_required(login_url='login')
def add_return(request):


    if request.method == 'POST':

        forms = supply_return_Form(request.POST)
        DC_date = request.POST.get('DC_date')

        date_time = numOfDays(DC_date)

        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)


        print('-----------------------------------------------date_time')
        print(date_time.date())
        print(date.today())
        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time})
        forms = supply_return_Form(updated_request)

        print(DC_date)

        if forms.is_valid():
            print('save')

            forms.save()

            a = forms.cleaned_data['company']
            b = forms.cleaned_data['company_goods']
            c = forms.cleaned_data['goods_company']
            d = forms.cleaned_data['agent']
            e = forms.cleaned_data['bags']

            try:

                test = stock.objects.get(company = a, company_goods = b, goods_company = c)

                test.total_bag = test.total_bag + e
                test.save()

                return redirect('list_return')

            except stock.DoesNotExist:

                test = stock.objects.create(company = a, company_goods = b, goods_company = c, total_bag = e)
                return redirect('list_inward')

        else:
            print(forms.error)

    else:

        forms = supply_return_Form()

        context = {
            'form': forms
        }
        return render(request, 'transactions/add_return.html', context)



@login_required(login_url='login')
def list_return(request):

    data = supply_return.objects.all()

    supply_return_filter_data = supply_return_filter()

    # inward_filter_data = inward_filter()

    print(data)

    agent_name = request.GET.get('agent_name')

    if agent_name:

        data = data.filter(agent__name__icontains=agent_name)


    company_data = company.objects.all()

    context = {
        'data': data,
        'company_data': company_data,
        'filter_return_supply' : supply_return_filter_data
    }

    return render(request, 'transactions/list_return.html', context)


@login_required(login_url='login')
def update_return(request, return_id):

    if request.method == 'POST':

        instance = supply_return.objects.get(id = return_id)

        company = request.POST.get('company')
        company_goods = request.POST.get('company_goods')
        goods_company = request.POST.get('goods_company')
        bags = request.POST.get('bags')
        
        DC_date = request.POST.get('DC_date')

        date_time = numOfDays(DC_date)

        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)


        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time})
        forms = supply_return_Form(updated_request, instance=instance)

        if forms.is_valid():

            instance = supply_return.objects.get(id = return_id)


            try:

                test = stock.objects.get(company = company, company_goods = company_goods, goods_company = goods_company)

                if int(instance.company.id) != int(company) or int(instance.company_goods.id) != int(company_goods) or int(instance.goods_company.id) != int(goods_company):
                
                    if test.total_bag >= int(bags):
                        test = stock.objects.get(company = company, company_goods = company_goods, goods_company = goods_company)
                        test.total_bag = test.total_bag - int(bags)
                        test.save()
                        stock_before = stock.objects.get(company = instance.company.id, company_goods = instance.company_goods.id, goods_company = instance.goods_company.id)
                        stock_before.total_bag = stock_before.total_bag + instance.bags
                        stock_before.save()

                        print('--------heheye----------')

                        forms.save()
                else:

                    if instance.bags != int(bags):
                        
                        test = stock.objects.get(company = company, company_goods = company_goods, goods_company = goods_company)

                        if instance.bags > int(bags):
                            minus_stock = instance.bags - int(bags)
                        else:
                            add_stock = int(bags) - instance.bags

                        if minus_stock:

                            if test.total_bag >= minus_stock:

                                test.total_bag = test.total_bag - minus_stock
                                test.save()
                                forms.save()

                                return redirect('list_return')

                            else:
                                
                                messages.error(request, "Outward is more than Stock")
                                print('Outward is more than Stock')
                                return redirect('list_return')

                    
                        else:

                            test.total_bag = test.total_bag + add_stock
                            test.save()
                            forms.save()

                            return redirect('list_return')


                    else:
                        forms.save()
                        return HttpResponseRedirect(reverse('list_return'))

            except stock.DoesNotExist:

                messages.error(request, 'no stock in inventory for outward')
                return redirect('list_return')


        else:

            print(forms.errors)

    else:

        instance = supply_return.objects.get(id = return_id)
        forms = supply_return_Form(instance = instance)
        comapnyID = forms.instance.company.id
        comapny_goods_ID = forms.instance.company_goods.id
        goods_company_ID = forms.instance.goods_company.id
        agent_ID = forms.instance.agent.id

        context = {
            'form': forms,
            'comapnyID' : comapnyID,
            'comapny_goods_ID' : comapny_goods_ID,
            'goods_company_ID' : goods_company_ID,
            'agent_ID' : agent_ID       
        }
        return render(request, 'transactions/update_return.html', context)


@login_required(login_url='login')
def delete_return(request, return_id):

    try:
        con = supply_return.objects.get(id = return_id)
        print(con)
        test = stock.objects.get(company = con.company, company_goods = con.company_goods, goods_company = con.goods_company)
        test.total_bag = test.total_bag - con.bags
        test.save()
        con.delete()

        return HttpResponseRedirect(reverse('list_return'))


    except:
        print('something went wrong')
        return HttpResponseRedirect(reverse('list_return'))
 
        


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


    
    filtered_data = list(filtered_data.values_list('DC_number', 'agent__name', 'agent__place', 'agent__taluka', 'agent__district', 'company_goods__name', 'goods_company__goods_company_name', 'bags'))

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
        vals1.append(i[6])
        vals1.append(i[7])

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

    outward_filterd_data = list(outward_filterd_data.values_list('DC_number', 'agent__name', 'agent__place', 'agent__taluka', 'agent__district', 'company_goods__name', 'goods_company__goods_company_name', 'bags'))
    # print(out)

    outward_filterd_data = list(map(list, outward_filterd_data))

    print('-------------------------------')
    print(outward_filterd_data)


    vals1 = []
    vals1.append("Serial")
    vals1.append("DC Number")
    vals1.append("Party Name")
    vals1.append("Party Place")
    vals1.append("Party Taluka")
    vals1.append("Party District")
    vals1.append("Crop")
    vals1.append("Variety")
    vals1.append('Packet')

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
        vals1.append(i[7])

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


    filtered_data = list(data.values_list('DC_number', 'agent__name', 'agent__place', 'agent__taluka', 'agent__district', 'company_goods__name', 'goods_company__goods_company_name', 'bags'))


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

    vals.append(vals1)
    print(vals)

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

    print('i am here')

    data = stock.objects.all()

    data_stock = stock_filter(request.GET, data)
    data_stock = data_stock.qs

    data1 = []
    data2 = []





    if data_stock:

        for i in data_stock:

            print('(i.company.company_name')
            print(i.company.company_name)

            data1.append(i.company.company_name)
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

    stock_filter_data = stock_filter()

    context = {
        'data': data2,
        'stock_filter' : stock_filter_data,
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

    print('outward_data')
    print(outward_data)
    print('supply_return_data')
    print(supply_return_data)
    if outward_data and not supply_return_data:
        
        # outward sum
        df2 = pd.DataFrame(list(outward_filterd_data.qs.values()))
        sum__ = df2.groupby(['company_id', 'company_goods_id', 'goods_company_id', 'agent_id']).sum().reset_index()
        print('df2--------newwwww-----------')
        print(sum__)

        sum__['bags_x'] = sum__['bags']
        sum__['bags_y'] = None
        sum__['bags_z'] = sum__['bags']
        sum__['company_id'] = sum__['company_id'].map(company_data)
        sum__['company_goods_id'] = sum__['company_goods_id'].map(company_goods_data)
        sum__['goods_company_id'] = sum__['goods_company_id'].map(goods_company_data)
        sum__['agent_id'] = sum__['agent_id'].map(agent_data)
        

        out = (sum__.merge(agent_data2, left_on='agent_id', right_on='name').reindex(columns=['agent_id', 'place', 'taluka', 'district', 'company_id', 'company_goods_id', 'goods_company_id', 'bags_x', 'bags_y', 'bags_z']))


      


    

        

      

        

        

    elif supply_return_data:
        #return sum
        df3 = pd.DataFrame(list(supply_return_filterd_data.qs.values()))
        sum__2 = df3.groupby(['company_id', 'company_goods_id', 'goods_company_id', 'agent_id']).sum().reset_index()

        print('return ')
        print(sum__2)

        vals = out.values


    else:


        final_ou = pd.merge(sum__, sum__2, on=['company_id', 'company_goods_id', 'goods_company_id', 'agent_id'], how="outer")[['company_id', 'company_goods_id', 'goods_company_id', 'agent_id', 'bags_x', 'bags_y']]
        final_ou['bags_z'] = final_ou.fillna(0)['bags_x'] - final_ou.fillna(0)['bags_y']

        
        print('stock ')
        print(final_ou)
        final_ou['company_id'] = final_ou['company_id'].map(company_data)
        final_ou['company_goods_id'] = final_ou['company_goods_id'].map(company_goods_data)
        final_ou['goods_company_id'] = final_ou['goods_company_id'].map(goods_company_data)
        final_ou['agent_id'] = final_ou['agent_id'].map(agent_data)

        # print(final_ou)
        # here
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
    print('--------------soukdgsbvhgdvei')

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
    print(inward_data)
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
    print('stock')
    print(sum__4)

    data_frames = [sum__, sum__2, sum__3, sum__4]

    ada = reduce(lambda  left,right: pd.merge(left,right,on=['company_id', 'company_goods_id', 'goods_company_id'], how='outer'), data_frames)[['company_id', 'company_goods_id', 'goods_company_id', 'bags_x', 'bags_y', 'bags', 'total_bag']]
    print('final')

    print(ada)

   

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

    inward_filter_data = inward_filter()

    context = {
        'data': data,
        'filter_inward' : inward_filter_data
    }

    return render(request, 'delete/list_inward_delete.html', context)


def list_outward_delete(request):

    data = outward.objects.all()

    outward_filter_data = outward_filter()



    context = {
        'data': data,
        'filter_outward' : outward_filter_data
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






