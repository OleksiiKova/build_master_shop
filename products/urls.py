from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/<str:variant_sku>/', views.product_detail, name='product_detail_variant'),
]