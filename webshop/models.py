from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """"
    Creating categories data model for the prints
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Print(models.Model):
    """
    Creating prints(products) data model
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='print_images')
    category = models.ForeignKey(Category, related_name='categories',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PrintOption(models.Model):
    """
    Creating sizes for prints data model
    """
    a4 = 'a4'
    a3 = 'a3'
    a3plus = 'a3+'

    SIZE_CHOICES = (
        (a4, 'A4'),
        (a3, 'A3'),
        (a3plus, 'A3+'),
    )
    size = models.CharField(max_length=255, choices=SIZE_CHOICES, default=a4)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.size
