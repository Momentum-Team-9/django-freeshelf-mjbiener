from django.shortcuts import render, get_object_or_404
from .models import User, Author, Book


# Create your views here.

# def index(request):
#     users = User.objects.all()

#     return render(request, 'books/index.html', {'users': users})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})