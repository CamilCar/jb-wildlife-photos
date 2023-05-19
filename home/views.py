from django.shortcuts import render
from orders.models import Order, OrderItem, ShippingInformation
from webshop.models import PrintOption

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


def policy(request):
    """ Returns policy info page """

    return render(request, 'delivery_info/policy.html')


def pricing(request):
    """ Returns prices page """

    return render(request, 'pricing/pricing.html')


def admin_page(request):
    """ Returns admin page """

    order_list = []

    orders = Order.objects.all()
    shipping_informations = ShippingInformation.objects.all()

    # for order in orders:
    #     #order.shipping_information
    #     order_items = order.prints.all()
    #     complete_order = {

    #     }
    #     print(order_items)

    return render(request, 'admin/admin_page.html', {
        "orders": orders
    })
