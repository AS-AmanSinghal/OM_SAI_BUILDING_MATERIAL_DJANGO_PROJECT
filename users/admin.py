from django.contrib import admin

from users.models import Customers, CustomerToken
from .forms import CustomerForm, CustomerEditForm


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')
    list_display_links = ('name', 'email')
    filter_horizontal = ()
    search_fields = ('email', 'name')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('profile_pic', 'name', 'mobile')}),
        ('Permissions', {'fields': ('is_active', 'date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',),
                'classes': ('wide',), }),
        ('Personal info', {'fields': ('profile_pic', 'name', 'mobile')}),
        ('Permissions', {'fields': 'is_active'}),
    )
    form = CustomerEditForm
    add_form = CustomerForm
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)


class CustomerTokenAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('customer',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('customer',)}),
    )
    readonly_fields = ('key',)


admin.site.register(Customers, CustomerAdmin)
admin.site.register(CustomerToken, CustomerTokenAdmin)
