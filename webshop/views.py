from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from .models import Category, Print, PrintOption

# Create your views here.


def webshop(request):
    """ Returns webshop page, including a category
    for filtering on page
    """
    prints = None
    categories = Category.objects.all()

    if 'category' in request.GET:
        categoryToFind = request.GET['category']
        prints = Print.objects.filter(category=categoryToFind)
    else:
        prints = Print.objects.all()

    return render(request, 'webshop/gallery.html', {
        'categories': categories,
        'prints': prints
    })


def product_detail(request, pk):
    """ Return product detail page with the correct product """
    product = get_object_or_404(Print, pk=pk)
    prices = serialize("json", PrintOption.objects.all())

    return render(request, 'webshop/product_detail.html', {
        'print': product,
        'prices': prices
    })
