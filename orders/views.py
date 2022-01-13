from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import DeleteWishlistForm, DeleteCartForm, OrderItemForm
from .models import Wishlist, Cart, Order, OrderItem


# Create your views here.


@login_required(login_url='login')
def wishlist(request):
    forms = DeleteWishlistForm()
    wishlist_data = Wishlist.objects.all()
    context = {
        'title': 'Wishlist',
        'wishlist_data': wishlist_data,
        'forms': forms
    }
    return render(request, 'adminhtml/order/wishlist.html', context)


@login_required(login_url='login')
def wishlist_delete(request, id):
    try:
        wishlist = get_object_or_404(Wishlist, id=id)
        wishlist.delete()
        messages.success(request, 'Wishlist has been deleted successfully.')
    except:
        messages.error(request, "Something went wrong.Try Again.")
    return redirect('wishlist')


@login_required(login_url='login')
def wishlist_all_delete(request):
    forms = DeleteWishlistForm()
    if request.method == 'POST':
        forms = DeleteWishlistForm(request.POST)
        if forms.is_valid():
            user_id = request.POST.get('user')
            Wishlist.objects.filter(user=user_id).delete()
            messages.success(request, "Wishlist has been deleted successfully.")
        else:
            messages.error(request, "Something went wrong. Try Again.")
    return redirect('wishlist')


@login_required(login_url='login')
def cart_list(request):
    cart_data = Cart.objects.all()
    for cart in cart_data:
        cart.sub_total = cart.quantity * cart.product.price
    forms = DeleteCartForm()
    context = {
        'title': 'Cart List',
        'forms': forms,
        'cart_data': cart_data
    }
    return render(request, 'adminhtml/order/cart/list.html', context)


@login_required(login_url='login')
def cart_delete(request, id):
    try:
        cart = get_object_or_404(Cart, id=id)
        cart.delete()
        messages.success(request, 'Cart has been deleted successfully.')
    except Exception as e:
        messages.error(request, e)
    return redirect('cart_list')


@login_required(login_url='login')
def cart_all_delete(request):
    forms = DeleteCartForm()
    if request.method == 'POST':
        forms = DeleteCartForm(request.POST)
        if forms.is_valid():
            user_id = request.POST.get('user')
            Cart.objects.filter(user=user_id).delete()
            messages.success(request, "Cart has been deleted successfully.")
        else:
            messages.error(request, forms.errors)
    return redirect('cart_list')


@login_required(login_url='login')
def order_list(request):
    order_data = Order.objects.all()
    context = {
        'title': 'Order List',
        'order_data': order_data
    }
    return render(request, 'adminhtml/order/list.html', context)


@login_required(login_url='login')
def order_item_list(request, order_id):
    orderitem_data = OrderItem.objects.filter(order__order_id=order_id)
    context = {
        'title': order_id,
        'orderitem_data': orderitem_data
    }
    return render(request, 'adminhtml/order/item/list.html', context)


@login_required(login_url='login')
def order_item_edit(request, id):
    try:
        order_item_data = get_object_or_404(OrderItem, id=id)
        forms = OrderItemForm(instance=order_item_data)
        if request.method == 'POST':
            forms = OrderItemForm(request.POST, instance=order_item_data)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Order item status has been changed successfully.')
            else:
                for field in forms:
                    for error in field.errors:
                        messages.error(request, error)
            return redirect('orderitem_list', order_id=order_item_data.order.order_id)
        context = {
            'title': order_item_data.product_name,
            'forms': forms
        }
        return render(request, 'adminhtml/users/add.html', context)
    except Exception as e:
        messages.error(request, e)
        return redirect('order_list')
