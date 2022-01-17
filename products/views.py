from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, UploadImagesForm
from .models import Product, Images


# Create your views here.
@login_required(login_url='login')
def product_list(request):
    product_data = Product.objects.all()
    context = {
        'title': 'Product List',
        'product_data': product_data
    }

    return render(request, 'adminhtml/product/list.html', context)


@login_required(login_url='login')
def product_status(request, id):
    flag = 1
    try:
        product = get_object_or_404(Product, id=id)
        if product.status:
            product.status = False
        else:
            if product.stock <= 0:
                product.status = False
                flag = 0
            else:
                product.status = True
        product.save()
        if flag:
            messages.success(request, "Product status has been updated successfully.")
        else:
            messages.error(request, "Product stock is less than or equals to zero.")
    except Exception as e:
        messages.error(request, e)
    return redirect('product_list')


@login_required(login_url='login')
def product_add(request):
    forms = ProductForm()
    UploadImagesFormSet = modelformset_factory(Images, form=UploadImagesForm, extra=5)
    formset = UploadImagesFormSet(queryset=Images.objects.none())
    if request.method == 'POST':
        forms = ProductForm(request.POST, request.FILES)
        formset = UploadImagesFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if forms.is_valid() and formset.is_valid():
            product = forms.save()
            for image_form in formset.cleaned_data:
                if image_form:
                    image = image_form['image']
                    photo = Images(product=product, image=image)
                    photo.save()
            messages.success(request, 'Product has been added successfully.')
            return redirect('product_list')
        else:
            for field in forms:
                for error in field.errors:
                    messages.error(request, error)
    context = {
        'title': 'Add Product',
        'forms': forms,
        'formset': formset
    }
    return render(request, 'adminhtml/product/add.html', context)


@login_required(login_url='login')
def product_delete(request, id):
    try:
        product_data = get_object_or_404(Product, id=id)
        product_data.delete()
        messages.success(request, "Product has been deleted successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('product_list')


@login_required(login_url='login')
def product_edit(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        forms = ProductForm(instance=product)
        if request.method == 'POST':
            forms = ProductForm(request.POST, request.FILES, instance=product)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Product has been updated successfully.")
                return redirect('product_list')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)

        context = {
            'title': product.name,
            'forms': forms
        }
    except Exception as e:
        messages.error(request, e)
        return redirect('product_list')
    return render(request, 'adminhtml/users/add.html', context)


@login_required(login_url='login')
def product_images_list(request, id):
    product_images_data = Images.objects.filter(product__id=id)
    context = {
        'title': 'Product Images List',
        'product_images_data': product_images_data
    }
    return render(request, 'adminhtml/product/images/list.html', context)


@login_required(login_url='login')
def product_images_edit(request, product_id, id):
    try:
        product_image_data = get_object_or_404(Images, id=id)
        forms = UploadImagesForm(instance=product_image_data)
        if request.method == 'POST':
            forms = UploadImagesForm(request.POST, request.FILES, instance=product_image_data)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Product image has been updated successfully.")
                return redirect('product_images_list', id=product_id)
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)
        context = {
            'title': product_image_data.product.name,
            'forms': forms
        }
        return render(request, 'adminhtml/users/add.html', context)
    except Exception as e:
        messages.error(request, e)
        return redirect('product_images_list', id=product_id)


@login_required(login_url='login')
def product_images_delete(request, product_id, id):
    try:
        product_image_data = get_object_or_404(Images, id=id)
        product_image_data.delete()
        messages.success(request, 'Product image has been deleted successfully.')
    except Exception as e:
        messages.error(request, e)
    return redirect('product_images_list', id=product_id)
