# Generated by Django 3.2.18 on 2023-04-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0010_cartitem_session_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('a4', 'A4'), ('a3', 'A3'), ('a3+', 'A3+')], default='a4', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
            ],
        ),
    ]