from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.http import HttpResponse

def index(request):
 return HttpResponse("Главная страница сайта Мир книг!")
