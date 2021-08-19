# Generated by Django 3.2.6 on 2021-08-19 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_rename_category_book_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
