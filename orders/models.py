from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from webshop.models import Print, PrintOption

# Create your models here.


class OrderItem(models.Model):
    """
    Creating orders item data model
    """
    print = models.ForeignKey(Print, on_delete=models.CASCADE,
                              related_name='prints')
    amount = models.IntegerField(default=1)
    print_option = models.ForeignKey(PrintOption, on_delete=models.CASCADE,
                                     related_name='print_options')

    def __str__(self):
        return f"{self.print.name} - id: {self.pk}"


class ShippingInformation(models.Model):
    """
    Creating shipping information data model
    """
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = PhoneNumberField(region="SE")
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address} {self.postal_code} {self.city}"


class Order(models.Model):
    """
    Creating orders data model
    """
    STATUS_OPTIONS = (
        ('new', 'New'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    prints = models.ManyToManyField(OrderItem, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_OPTIONS,
                              default='new')
    shipping_information = models.ForeignKey(ShippingInformation,
                                             on_delete=models.CASCADE,
                                             related_name='shipping_information')

    @property
    def total_price(self):
        prints = self.prints.all()
        total = sum(print.price for print in prints)
        return total

    def __str__(self):
        return f"{self.user.get_full_name()} - {str(self.pk)}"
