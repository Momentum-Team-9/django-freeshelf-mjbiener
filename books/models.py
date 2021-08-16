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

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=2500)
    release_year = models.IntegerField(blank=True, null=True)
    cover_photo = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.author}, {self.release_year}"