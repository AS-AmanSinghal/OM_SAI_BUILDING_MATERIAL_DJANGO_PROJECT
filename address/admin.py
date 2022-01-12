from django.contrib import admin

from .models import Address, ShippingCharges

# Register your models here.
admin.site.register(Address)
admin.site.register(ShippingCharges)
