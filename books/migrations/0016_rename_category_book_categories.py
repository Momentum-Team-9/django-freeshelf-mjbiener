# Generated by Django 3.2.6 on 2021-08-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20210818_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='categories',
        ),
    ]