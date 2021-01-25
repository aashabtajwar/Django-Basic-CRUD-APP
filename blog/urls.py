# this file is needed to map urls
# within this app

from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.apiOverview, name='blog-api'),
    path('posts/', views.getPosts, name='blog-posts'),
    path('post/<str:pk>/', views.getOnePost, name='blog-post'),
    path('write-post/', views.writeBlogPost, name='write-blog-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-post'),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('writeblog/', views.writeBlog, name='blog-writeBlog'),
    path('write/', views.writepost, name='blog-write')
]