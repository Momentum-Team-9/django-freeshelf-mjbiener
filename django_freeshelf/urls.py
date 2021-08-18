"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from books import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/books/', views.books_for_author, name='books_for_author'),
    path('categories/',views.categories, name='categories'),
    path('categories/<int:pk>/books/', views.books_in_category, name='books_in_category'),
]
