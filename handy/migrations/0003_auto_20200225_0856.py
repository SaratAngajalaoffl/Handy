# Generated by Django 3.0.2 on 2020-02-25 08:56

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('handy', '0002_auto_20200224_1016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artisans',
            new_name='Artisan',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
