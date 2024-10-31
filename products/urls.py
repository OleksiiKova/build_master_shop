from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="products"),
    path('add/', views.add_product, name="add_product"),
    path('edit/<str:sku>/', views.edit_product, name='edit_product'),
    path('delete/<str:sku>/', views.delete_product, name='delete_product'),
    path('<str:sku>/', views.product_detail_by_sku,
         name='product_detail_by_sku'),
]
