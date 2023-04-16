from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returns index page """

    return render(request, 'home/index.html')


def contact(request):
    """ Returns contact page """

    return render(request, 'contact/contact.html')
