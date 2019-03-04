from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myBlogPosts/', views.myBlogPosts, name='myBlogPosts'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]