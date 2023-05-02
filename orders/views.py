from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cart.contexts import cart_content
from cart.forms import ConfirmBookingForm

from orders.models import Order, OrderItem
from webshop.models import PrintOption

# Create your views here.


@login_required
def create_order(request):
    shipping_information_form = ConfirmBookingForm(request.POST)

    if shipping_information_form.is_valid():
        new_shipping_information = shipping_information_form.save()
        cart = cart_content(request)

        user = request.user
        new_order = Order(user=user,
                          shipping_information=new_shipping_information)
        new_order.save()

        for item in cart['cart_items']:
            print_option = get_object_or_404(PrintOption, size=item['size'])
            new_cart_item = OrderItem(print=item['print'],
                                      amount=item['quantity'],
                                      print_option=print_option
                                      )
            new_cart_item.save()
            new_order.prints.add(new_cart_item)

        return render(request, 'orders/thanks_for_order.html')
    return redirect(request.META['HTTP_REFERER'])
