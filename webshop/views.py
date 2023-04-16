from django.shortcuts import render
from .models import Print, Category

# Create your views here.


def webshop(request):
    """ Returns webshop page """
    prints = Print.objects.all()
    categories = Category.objects.all()

    return render(request, 'webshop/gallery.html', {
        'categories': categories,
        'prints': prints
    })
