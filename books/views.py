from django.shortcuts import redirect, render, get_object_or_404
from .models import User, Author, Book, Category


# Create your views here.

def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('book_list')
    return render(request, 'books/index.html', {'users': users})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def author_list(request):
    authors = Author.objects.all()

    return render(request, 'books/author_list.html', {'authors': authors})


def books_for_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(request, 'books/books_for_author.html', {'books': books})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'books/categories.html', {'categories': categories})


def show_categories(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    books = categories.books.all()

    return render(request, "books/show_categories.html", {"categories": categories, "books": books})
