# Generated by Django 3.2.18 on 2023-04-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
