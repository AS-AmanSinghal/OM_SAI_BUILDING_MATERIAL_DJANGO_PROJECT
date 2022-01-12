from django.db import models

from users.models import Customers


# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    mobile = models.CharField(max_length=10, blank=False)
    alternative_mobile = models.CharField(max_length=10, blank=True)
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    landmark = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    pincode = models.CharField(max_length=6, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'


class ShippingCharges(models.Model):
    pincode = models.CharField(max_length=6, blank=False, unique=True)
    charges = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pincode}'

    class Meta:
        verbose_name = 'shipping charge'
        verbose_name_plural = 'shipping charges'
