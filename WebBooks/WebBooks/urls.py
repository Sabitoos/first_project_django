from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'^books/', views.BookListView.as_view(), name='books'),
    re_path(r'^book-detail/', views.BookDetailView.as_view(), name='book-detail'),
]