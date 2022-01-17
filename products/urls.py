from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('add/', views.product_add, name='product_add'),
    path('edit/id/<int:id>', views.product_edit, name='product_edit'),
    path('status/id/<int:id>', views.product_status, name='product_status'),
    path('delete/id/<int:id>', views.product_delete, name='product_delete'),
    path('product/image/list/product/id/<int:id>', views.product_images_list, name='product_images_list'),
    path('product/image/edit/product/id/<int:product_id>/id/<int:id>', views.product_images_edit,
         name='product_images_edit'),
    path('product/images/delete/product/id/<int:product_id>/id/<int:id>', views.product_images_delete,
         name='product_images_delete'),
]
