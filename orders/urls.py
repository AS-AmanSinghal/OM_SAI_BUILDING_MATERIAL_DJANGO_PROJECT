from django.urls import path

from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/delete/id/<int:id>', views.wishlist_delete, name='wishlist_delete'),
    path('wishlist/delete/', views.wishlist_all_delete, name='wishlist_all_delete'),
    path('cart/list/', views.cart_list, name='cart_list'),
    path('cart/delete/id/<int:id>', views.cart_delete, name='cart_delete'),
    path('cart/delete/', views.cart_all_delete, name='cart_all_delete'),
    path('list/', views.order_list, name='order_list'),
    path('item/list/order_id/<str:order_id>/', views.order_item_list, name='orderitem_list'),
    path('item/edit/id/<int:id>/', views.order_item_edit, name='order_item_edit'),
]
