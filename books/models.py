from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField, URLField
from django.urls import reverse


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(max_length=100)
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
    categories = models.ManyToManyField('Category', related_name="books", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # favorited_by = models.ManyToManyField("User", related_name="favorite_books")

    def __str__(self):

        return f"{self.title}, {self.authors.all()[0].name}, {self.release_year}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length= 50, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("show_category", kwargs={"slug": self.slug})

    def __repr__(self):
        return f"<Category name ={self.name}>"

    def __str__(self):
        return f'{self.name}'