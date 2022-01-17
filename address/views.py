from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ShippingChargeForm
from .models import Address, ShippingCharges


# Create your views here.


@login_required(login_url='login')
def address_list(request):
    address_data = Address.objects.all()
    context = {
        'title': 'Address List',
        'address_data': address_data
    }
    return render(request, 'adminhtml/address/list.html', context)


@login_required(login_url='login')
def address_status(request, id):
    try:
        address_data = get_object_or_404(Address, id=id)
        if address_data.status:
            address_data.status = False
        else:
            address_data.status = True
        address_data.save()
        messages.success(request, "Address status has been changed successfully.")
    except Exception as e:
        messages.error(request, e)
    return redirect('address_list')


@login_required(login_url='login')
def address_delete(request, id):
    try:
        address_data = get_object_or_404(Address, id=id)
        address_data.delete()
        messages.success(request, 'Address has been deleted successfully.')
    except Exception as e:
        messages.error(request, e)
    return redirect('address_list')


@login_required(login_url='login')
def shipping_charge_list(request):
    shipping_charge_data = ShippingCharges.objects.all()
    context = {
        'title': 'Shipping Charge List',
        'shipping_charge_data': shipping_charge_data
    }
    return render(request, 'adminhtml/shipping/list.html', context)


@login_required(login_url='login')
def shipping_charge_status(request, id):
    try:
        shipping_charge_data = get_object_or_404(ShippingCharges, id=id)
        if shipping_charge_data.status:
            shipping_charge_data.status = False
        else:
            shipping_charge_data.status = True
        shipping_charge_data.save()
        messages.success(request, "Shipping Charge status has been changed successfully.")
    except Exception as e:
        messages.error(request, e)
    return redirect('shipping_charge_list')


@login_required(login_url='login')
def shipping_charge_delete(request, id):
    try:
        shipping_charge_data = get_object_or_404(ShippingCharges, id=id)
        shipping_charge_data.delete()
        messages.success(request, 'Shipping charge has been deleted successfully.')
    except Exception as e:
        messages.error(request, e)
    return redirect('shipping_charge_list')


@login_required(login_url='login')
def shipping_charge_add(request):
    forms = ShippingChargeForm()

    if request.method == 'POST':
        forms = ShippingChargeForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Shipping Charge has been saved successfully.")
            return redirect('shipping_charge_list')
        else:
            for field in forms:
                for error in field.errors:
                    messages.error(request, error)

    context = {
        'title': 'Add Shipping Charge',
        'forms': forms
    }
    return render(request, 'adminhtml/users/add.html', context)


@login_required(login_url='login')
def shipping_charge_edit(request, id):
    try:
        shipping_charge_data = get_object_or_404(ShippingCharges, id=id)
        forms = ShippingChargeForm(instance=shipping_charge_data)
        if request.method == 'POST':
            forms = ShippingChargeForm(request.POST, instance=shipping_charge_data)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Shipping charge has been updated successfully.")
                return redirect('shipping_charge_list')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)
    except Exception as e:
        messages.error(request, e)
        return redirect('shipping_charge_list')
    context = {
        'title': shipping_charge_data.pincode,
        'forms': forms
    }
    return render(request, 'adminhtml/users/add.html', context)
