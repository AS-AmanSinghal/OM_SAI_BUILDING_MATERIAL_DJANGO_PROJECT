from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

# from address.models import Address, ShippingCharges
# from category.models import Category, SubCategory, Brand
# from orders.models import Order
# from products.models import Product
from users.models import Customers


@login_required(login_url='login')
def home(request):
    customer_count = Customers.objects.all().count()
    # address_count = Address.objects.all().count()
    # shipping_count = ShippingCharges.objects.all().count()
    # category_count = Category.objects.all().count()
    # sub_category_count = SubCategory.objects.all().count()
    # brand_count = Brand.objects.all().count()
    # product_count = Product.objects.all().count()
    # order_count = Order.objects.all().count()

    context = {
        'title': 'Dashboard',
        'customer_count': customer_count,
        # 'address_count': address_count,
        # 'shipping_count': shipping_count,
        # 'category_count': category_count,
        # 'sub_category_count': sub_category_count,
        # 'brand_count': brand_count,
        # 'product_count': product_count,
        # 'order_count': order_count
    }
    return render(request, 'adminhtml/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request=request, user=user)
                client_ip = request.META['REMOTE_ADDR']
                browser = request.headers['User-Agent']
                try:
                    data = {
                        'ip_address': client_ip,
                        'browser': browser,
                        'user': user,
                        'time': user.last_login,
                        'domain': get_current_site(request),
                    }
                    subject = 'Login Alert'
                    html_body = render_to_string('adminhtml/email/login.html', data)
                    msg = EmailMultiAlternatives(subject=subject, to=[user.email])
                    msg.attach_alternative(html_body, 'text/html')
                    msg.send()
                    messages.success(request, "Email has been send successfully.")
                except Exception as e:
                    messages.error(request, e)
                return redirect('home')

    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'adminhtml/login/login.html')


@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')
