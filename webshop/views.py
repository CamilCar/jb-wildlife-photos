from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.


def webshop(request):
    """ Returns webshop page """

    return render(request, 'webshop/gallery.html')
