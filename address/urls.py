from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.address_list, name='address_list'),
    path('status/id/<int:id>/', views.address_status, name='address_status'),
    path('delete/id/<int:id>/', views.address_delete, name='address_delete'),
    path('shipping/charge/list/', views.shipping_charge_list, name='shipping_charge_list'),
    path('shipping/charge/status/id/<int:id>/', views.shipping_charge_status, name='shipping_charge_status'),
    path('shipping/charge/delete/id/<int:id>/', views.shipping_charge_delete, name='shipping_charge_delete'),
    path('shipping/charge/add/', views.shipping_charge_add, name='shipping_charge_add'),
    path('shipping/charge/edit/id/<int:id>/', views.shipping_charge_edit, name='shipping_charge_edit'),
]
