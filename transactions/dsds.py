
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

    product_qr_old = product_qr_old = copy.copy(product_qr_instance)

    print('here checking')
    print(product_qr_old.is_fix)

    if request.method == 'POST':

        form = product_Form(request.POST)

        if form.is_valid():
            book, created = product.objects.get_or_create(**form.cleaned_data)


            form2 = product_qr_Form(request.POST, request.FILES, instance = product_qr_instance)
            if form2.is_valid():

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
            

                if book:

                    product_instance = book

                else:

                    product_instance = created

                messages.success(request, 'values added successfully')

                instance, created = stock.objects.get_or_create(product = product_instance)

                print('-----------------------')
                print('-----------------------')
                print(product_qr_old.is_fix)
                print('-----------------------')
                print('-----------------------')
                
                if product_qr_old.is_fix:

                    print('-----------------------')
                    print('-----------------------')
                    print('-----------------------')
                    print('-----------------------')
                    print('-----------------------')
                
                    instance_previous_stock = stock.objects.get(product = product_qr_old.product)
                    instance_previous_stock.quantity = instance_previous_stock.quantity - 1
                    instance_previous_stock.save()
                
                if instance:

                    instance.quantity = instance.quantity + 1
                    instance.save()

                else:

                    created.quantity = 1
                    created.save()


                product_qr_instance.product = product_instance
                product_qr_instance.is_fix = True
                product_qr_instance.save()

                redirect_url = reverse('list_generated_product_qr')

                return redirect(redirect_url)
