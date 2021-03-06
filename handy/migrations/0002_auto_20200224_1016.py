# Generated by Django 3.0.2 on 2020-02-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('handy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='handy.Category'),
        ),
    ]
