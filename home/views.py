from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returns index page """

    return render(request, 'home/index.html')


def contact(request):
    """ Returns contact page """

    return render(request, 'contact/contact.html')


def about(request):
    """ Returns about page """

    return render(request, 'about/about.html')


def delivery(request):
    """ Returns delivery info page """

    return render(request, 'delivery_info/delivery.html')


def pricing(request):
    """ Returns prices page """

    return render(request, 'pricing/pricing.html')
