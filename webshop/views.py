import json
from django.shortcuts import get_object_or_404, redirect, render

from .models import Print, Category

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

    prices = {
        'a4': 30,
        'a3': 40,
        'a3+': 50,
    }

    return render(request, 'webshop/product_detail.html', {
        'print': product,
        'prices': json.dumps(prices)
    })


def add_to_cart(request):
    print_id = request.POST['print_id']

    return redirect("product_detail/" + print_id)
