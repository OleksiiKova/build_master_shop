from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('order_history/<order_number>',
         views.order_history, name="order_history"),
    path('user-reviews/', views.user_reviews, name='user_reviews'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('review/edit/<int:review_id>/',
         views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/',
         views.delete_review, name='delete_review'),
    path('remove-from-wishlist/<int:item_id>/',
         views.remove_from_wishlist, name='remove_from_wishlist'),
]
