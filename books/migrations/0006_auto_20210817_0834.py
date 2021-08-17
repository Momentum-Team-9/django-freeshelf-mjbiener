# Generated by Django 3.2.6 on 2021-08-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='books', to='books.Category'),
        ),
    ]