# Generated by Django 3.0.4 on 2020-03-08 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_images', upload_to=''),
        ),
    ]
