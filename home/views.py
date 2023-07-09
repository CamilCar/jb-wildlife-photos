from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from cart.forms import ConfirmBookingForm
from orders.models import Order

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


@login_required
def my_orders(request):
    """ Returns my orders page to see all historical orders for the logged in user """

    orders = Order.objects.filter(user=request.user)

    return render(request, 'my_orders/my_orders.html', {
        "orders": orders
    })


@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    """ Returns admin page """

    orders = Order.objects.all()

    return render(request, 'admin/admin_page.html', {
        "orders": orders
    })

# Allows admin to update order status
@user_passes_test(lambda u: u.is_superuser)
def update_status(request, order_id, new_status):
    order = get_object_or_404(Order, pk=order_id)

    order.status = new_status
    order.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
