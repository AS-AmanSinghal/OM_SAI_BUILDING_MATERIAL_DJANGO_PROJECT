from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.category_add, name='category_add'),
    path('status/id/<int:id>/', views.category_status, name='category_status'),
    path('delete/id/<int:id>/', views.category_delete, name='category_delete'),
    path('edit/id/<int:id>/', views.category_edit, name='category_edit'),
    path('subcategory/add/', views.sub_category_add, name='sub_category_add'),
    path('subcategory/status/id/<int:id>/', views.sub_category_status, name='sub_category_status'),
    path('subcategory/delete/id/<int:id>/', views.sub_category_delete, name='sub_category_delete'),
    path('subcategory/edit/id/<int:id>/', views.sub_category_edit, name='sub_category_edit'),
    path('brand/add/', views.brand_add, name='brand_add'),
    path('brand/status/id/<int:id>/', views.brand_status, name='brand_status'),
    path('brand/delete/id/<int:id>/', views.brand_delete, name='brand_delete'),
    path('brand/edit/id/<int:id>/', views.brand_edit, name='brand_edit'),
    path('subcategory/filter/', views.brand_filter, name='brand_filter'),
]
