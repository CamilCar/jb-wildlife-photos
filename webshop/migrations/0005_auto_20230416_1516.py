# Generated by Django 3.2.18 on 2023-04-16 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0004_auto_20230416_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='print',
            name='price',
        ),
        migrations.RemoveField(
            model_name='print',
            name='size',
        ),
    ]