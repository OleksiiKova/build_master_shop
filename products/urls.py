from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="products"),
    path('<str:sku>/', views.product_detail_by_sku, name='product_detail_by_sku'),
    # path('<int:product_id>/', views.product_detail, name='product_detail'),
    # path('<int:product_id>/<str:variant_sku>/', views.product_detail, name='product_detail_variant'),
]