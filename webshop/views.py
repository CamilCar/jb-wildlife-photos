from django.shortcuts import render

# Create your views here.


def webshop(request):
    """ Returns webshop page """

    return render(request, 'webshop/gallery.html')