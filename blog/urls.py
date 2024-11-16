from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_blog_posts, name='all_blog_posts'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('<slug:slug>/', views.blog_post, name='blog_post'),
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<slug:slug>/',
         views.delete_blog_post, name='delete_blog_post'),
]
