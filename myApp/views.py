from django.shortcuts import render
from django.views.generic import ListView, DetailView
from myApp.models import Book

# Create your views here.
class BookListView(ListView):

    model = Book
    # template_name = 'myApp/books.html'
    # context_object_name = 'list_of_book'

class DetailView(DetailView):

    model = Book

