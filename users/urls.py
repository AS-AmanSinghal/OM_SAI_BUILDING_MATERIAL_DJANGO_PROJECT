from django.urls import path

from . import views

urlpatterns = [
    path('customer/list/', views.customer_list, name='customer_list'),
    path('customer/status/id/<int:id>/', views.customer_status, name='customer_status'),
    path('customer/delete/id/<int:id>/', views.customer_delete, name='customer_delete'),
    path('customer/add/', views.customer_add, name='customer_add'),
    path('customer/edit/id/<int:id>/', views.customer_edit, name='customer_edit'),
]
