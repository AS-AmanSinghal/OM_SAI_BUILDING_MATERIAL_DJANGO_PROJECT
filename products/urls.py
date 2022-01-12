from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('add/', views.product_add, name='product_add'),
    path('edit/id/<int:id>', views.product_edit, name='product_edit'),
    path('status/id/<int:id>', views.product_status, name='product_status'),
    path('delete/id/<int:id>', views.product_delete, name='product_delete'),
    path('images/list/', views.product_images_list, name='product_images_list'),
    path('images/edit/id/<int:id>', views.product_images_edit, name='product_images_edit'),
    path('images/delete/id/<int:id>', views.product_images_delete, name='product_images_delete'),
]
