from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views

urlpatterns = [
 path('', views.index),
 re_path(r'^about', views.about),
 re_path(r'^contact', views.contact),
 path('products/', views.products), # маршрут по умолчанию
 path('products/<int:productid>/', views.products),
 path('users/', views.users), # маршрут по умолчанию
 path('users/<int:id>/<str:name>/', views.users),
]