from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CategoryForm, SubCategoryForm, BrandForm
from .models import Category, SubCategory, Brand


# Create your views here.


@login_required(login_url='login')
def category_add(request):
    forms = CategoryForm()
    category_data = Category.objects.all()
    if request.method == 'POST':
        forms = CategoryForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Category has been added successfully.')
            return redirect('category_add')
        else:
            for field in forms:
                for error in field.errors:
                    messages.error(request, error)
    context = {
        'title': 'Category List',
        'category_data': category_data,
        'forms': forms
    }
    return render(request, 'adminhtml/category/add.html', context)


@login_required(login_url='login')
def category_status(request, id):
    try:
        category_data = get_object_or_404(Category, id=id)
        if category_data.status:
            category_data.status = False
        else:
            category_data.status = True
        category_data.save()
        messages.success(request, "Category status has been updated successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('category_add')


@login_required(login_url='login')
def category_delete(request, id):
    try:
        category_data = get_object_or_404(Category, id=id)
        category_data.delete()
        messages.success(request, "Category has been deleted successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('category_add')


@login_required(login_url='login')
def category_edit(request, id):
    category_data = Category.objects.all()
    try:
        category = get_object_or_404(Category, id=id)
        forms = CategoryForm(instance=category)
        if request.method == 'POST':
            forms = CategoryForm(request.POST, request.FILES, instance=category)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Category has been updated successfully.")
                return redirect('category_add')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)

        context = {
            'title': category.name,
            'forms': forms,
            'category_data': category_data
        }
    except Exception as e:
        messages.error(request, e)
        return redirect('category_add')
    return render(request, 'adminhtml/category/add.html', context)


@login_required(login_url='login')
def sub_category_add(request):
    forms = SubCategoryForm()
    sub_category_data = SubCategory.objects.all()
    if request.method == 'POST':
        forms = SubCategoryForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Sub category has been added successfully.')
            return redirect('sub_category_add')
        else:
            for field in forms:
                for error in field.errors:
                    messages.error(request, error)
    context = {
        'title': 'Sub Category List',
        'sub_category_data': sub_category_data,
        'forms': forms
    }
    return render(request, 'adminhtml/subcategory/add.html', context)


@login_required(login_url='login')
def sub_category_status(request, id):
    try:
        sub_category_data = get_object_or_404(SubCategory, id=id)
        if sub_category_data.status:
            sub_category_data.status = False
        else:
            sub_category_data.status = True
        sub_category_data.save()
        messages.success(request, "Sub category status has been updated successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('sub_category_add')


@login_required(login_url='login')
def sub_category_delete(request, id):
    try:
        sub_category_data = get_object_or_404(SubCategory, id=id)
        sub_category_data.delete()
        messages.success(request, "Sub category has been deleted successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('sub_category_add')


@login_required(login_url='login')
def sub_category_edit(request, id):
    sub_category_data = SubCategory.objects.all()
    try:
        sub_category = get_object_or_404(SubCategory, id=id)
        forms = SubCategoryForm(instance=sub_category)
        if request.method == 'POST':
            forms = SubCategoryForm(request.POST, request.FILES, instance=sub_category)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Sub category has been updated successfully.")
                return redirect('sub_category_add')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)

        context = {
            'title': sub_category.name,
            'forms': forms,
            'sub_category_data': sub_category_data
        }
    except Exception as e:
        messages.error(request, e)
        return redirect('sub_category_add')
    return render(request, 'adminhtml/subcategory/add.html', context)


@login_required(login_url='login')
def brand_add(request):
    forms = BrandForm()
    brand_data = Brand.objects.all()
    if request.method == 'POST':
        forms = BrandForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Brand has been added successfully.')
            return redirect('brand_add')
        else:
            for field in forms:
                for error in field.errors:
                    messages.error(request, error)
    context = {
        'title': 'Brand List',
        'brand_data': brand_data,
        'forms': forms
    }
    return render(request, 'adminhtml/brand/add.html', context)


@login_required(login_url='login')
def brand_status(request, id):
    try:
        brand_data = get_object_or_404(Brand, id=id)
        if brand_data.status:
            brand_data.status = False
        else:
            brand_data.status = True
        brand_data.save()
        messages.success(request, "Brand status has been updated successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('brand_add')


@login_required(login_url='login')
def brand_delete(request, id):
    try:
        brand_data = get_object_or_404(Brand, id=id)
        brand_data.delete()
        messages.success(request, "Brand has been deleted successfully.")
    except Exception as e:
        messages.success(request, e)
    return redirect('brand_add')


@login_required(login_url='login')
def brand_edit(request, id):
    brand_data = Brand.objects.all()
    try:
        brand = get_object_or_404(Brand, id=id)
        forms = BrandForm(instance=brand)
        if request.method == 'POST':
            forms = BrandForm(request.POST, request.FILES, instance=brand)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Brand has been updated successfully.")
                return redirect('brand_add')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)

        context = {
            'title': brand.brand_name,
            'forms': forms,
            'brand_data': brand_data
        }
    except Exception as e:
        messages.error(request, e)
        return redirect('brand_add')
    return render(request, 'adminhtml/brand/add.html', context)


@login_required(login_url='login')
def brand_filter(request):
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            brand_data = Brand.objects.filter(sub_category__id=id)
            return JsonResponse(data={'data': serializers.serialize('json', brand_data, fields=('brand_name',))})
        except Exception as e:
            pass
    return JsonResponse(data={'data': ""})
