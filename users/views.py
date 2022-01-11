from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomerForm, CustomerEditForm
from .models import Customers, send_customer_email


# Create your views here.

@login_required(login_url='login')
def customer_list(request):
    customer_data = Customers.objects.all()
    context = {
        'title': 'Customers List',
        'customer_data': customer_data
    }
    return render(request, 'adminhtml/users/list.html', context)


@login_required(login_url='login')
def customer_status(request, id):
    try:
        customer_data = get_object_or_404(Customers, id=id)
        if customer_data.is_active:
            customer_data.is_active = False
        else:
            customer_data.is_active = True
        customer_data.save()
        messages.success(request, "Customer status has been changed successfully.")
    except:
        messages.error(request, "Something Went Wrong.Try Again.")
    return redirect('customer_list')


@login_required(login_url='login')
def customer_delete(request, id):
    try:
        customer_data = get_object_or_404(Customers, id=id)
        customer_data.delete()
        messages.success(request, "Customer has been deleted successfully.")
    except:
        messages.error(request, "Something went wrong.Try Again.")
    return redirect('customer_list')


@login_required(login_url='login')
def customer_add(request):
    forms = CustomerForm()
    if request.method == 'POST':
        forms = CustomerForm(request.POST, request.FILES)
        if forms.is_valid():
            users = forms.save()
            send_customer_email(users, request.META['REMOTE_ADDR'], request.headers['User-Agent'],
                                get_current_site(request), request.POST.get('password1'))
            messages.success(request, "Customer has been saved successfully.")
            return redirect('customer_list')
        else:
            for field in forms:
                for error in field.errors:
                    messages.error(request, error)
    context = {
        'title': 'Add Customer',
        'forms': forms
    }
    return render(request, 'adminhtml/users/add.html', context)


@login_required(login_url='login')
def customer_edit(request, id):
    try:
        customer_data = get_object_or_404(Customers, id=id)
        forms = CustomerEditForm(instance=customer_data)
        if request.method == 'POST':
            forms = CustomerEditForm(request.POST, request.FILES, instance=customer_data)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Customer has been updated successfully.")
                return redirect('customer_list')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)
        context = {
            'title': customer_data.name,
            'forms': forms
        }
    except Exception as e:
        messages.error(request, e)
        return redirect('customer_list')

    return render(request, 'adminhtml/users/add.html', context)
