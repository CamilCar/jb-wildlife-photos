from django.shortcuts import get_object_or_404, render

from .models import Category, Print, PrintOption

# Create your views here.


def webshop(request):
    """ Returns webshop page, including filter """
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
    product = get_object_or_404(Print, pk=pk)
    prices = PrintOption.objects.all()

    return render(request, 'webshop/product_detail.html', {
        'print': product,
        'prices': prices
    })
