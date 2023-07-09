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


@login_required
def edit_order(request, order_id):
    """ Returns my orders page to see all historical orders for the logged in user """
    order = get_object_or_404(Order, pk=order_id)

    shipping_information_form = None
    shipping_form_not_valid = False

    if request.POST:
        shipping_information_form = ConfirmBookingForm(request.POST)

        if shipping_information_form.is_valid():
            shipping_information_form.save()
        else:
            shipping_form_not_valid = True
            shipping_information_form = ConfirmBookingForm(instance=order.shipping_information)
    else:
        shipping_information_form = ConfirmBookingForm(instance=order.shipping_information)

    return render(request, 'my_orders/edit_order.html', {
        "order": order,
        "shipping_information_form": shipping_information_form,
        "shipping_form_not_valid": shipping_form_not_valid
    })


@login_required
def delete_order(request, order_id):
    """ Deletes an order from the database and returns my orders page """

    order_to_delete = get_object_or_404(Order, pk=order_id)  

    order_to_delete.prints.all().delete()
    order_to_delete.shipping_information.delete()

    order_to_delete.delete()

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

