from django.db import models

from products.models import Product
from users.models import Customers


# Create your models here.


class Wishlist(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.name}'

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'


class Cart(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.name}'

    def save(self, *args, **kwargs):
        try:
            data = Cart.objects.get(user=self.user, product=self.product)
            if self.pk is None:
                data.quantity += self.quantity
                super(Cart, data).save(*args, **kwargs)
            else:
                super(Cart, self).save(*args, **kwargs)
        except:
            super(Cart, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'


class Order(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, default='', unique=True, blank=False, null=False)
    mode_of_payment = models.CharField(max_length=20, null=False, blank=False)
    customer_name = models.CharField(max_length=20, blank=False, null=False)
    mobile = models.CharField(max_length=10, blank=False, null=False)
    alternative_mobile = models.CharField(max_length=10, blank=False, null=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    landmark = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    pincode = models.CharField(max_length=6, null=False, blank=False)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer_name}'


class OrderItem(models.Model):
    STATUS = [
        ('Order not confirm', 'Order not confirm'),
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Complete', 'Complete'),
        ('Delivered', 'Delivered'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, null=False, blank=False)
    price = models.PositiveIntegerField()
    discount = models.DecimalField(decimal_places=2, max_digits=10000)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name}'
