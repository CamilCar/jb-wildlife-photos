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
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    """
    Adds cart item in db
    """
    print = models.ForeignKey(Print, on_delete=models.CASCADE, related_name='prints')
    size = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.print.name


class Cart(models.Model):
    """
    Adds cart in db
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    prints = models.ManyToManyField(CartItem, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    session_key = models.CharField(max_length=40, null=True)

    def __int__(self):
        return self.pk

    @property
    def total_price(self):
        prints = self.prints.all()
        total = sum(print.price for print in prints)
        return total

    @property
    def amount_of_prints(self):
        prints = self.prints.all()
        amount = sum(print.amount for print in prints)
        return amount
