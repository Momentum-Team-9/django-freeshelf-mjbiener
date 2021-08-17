from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField, URLField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(max_length=100)
    # books = models.ManyToManyField(Book, related_name="authors")
    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    # books = models.ManyToManyField(Book, related_name="authors")
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(Author, related_name='books', blank=True)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=2500)
    release_year = models.IntegerField(blank=True, null=True)
    cover_photo = models.CharField(max_length=250, blank=True, null=True)
    category = models.ManyToManyField('Category', related_name="books", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # favorited_by = models.ManyToManyField("User", related_name="favorite_books")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}, {self.authors}, {self.release_year}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f'{self.name}'