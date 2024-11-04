from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="products"),
    path('add/', views.add_product, name="add_product"),
    path('edit/<str:sku>/', views.edit_product, name='edit_product'),
    path('delete/<str:sku>/', views.delete_product, name='delete_product'),
    path('<str:sku>/', views.product_detail_by_sku,
         name='product_detail_by_sku'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
