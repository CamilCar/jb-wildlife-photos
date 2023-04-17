from django.db import models


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
