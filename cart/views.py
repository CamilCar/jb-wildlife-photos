from django.shortcuts import get_object_or_404, render, redirect
from cart.forms import ConfirmBookingForm

from webshop.models import PrintOption

# Create your views here.


def view_cart(request):
    """ Returns cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, print_id):
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    print_option = get_object_or_404(PrintOption, size=size)
    print_size_id = print_option.id

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    print_key = f"{print_id}{print_size_id}"

    if print_key in list(cart.keys()):
        cart[print_key]['quantity'] += quantity

    else:
        cart_details = {
            'id': print_id,
            'quantity': quantity,
            'size': size
        }
        cart[print_key] = cart_details

    request.session['cart'] = cart
    return redirect(redirect_url)


def checkout(request):
    return render(request, 'cart/checkout.html')


def checkout_continue(request):
    if request.user.is_authenticated:
        shipping_information_form = ConfirmBookingForm()
        return render(request, 'cart/checkout.html', {
            'shipping_information': shipping_information_form
        })
    else:
        # prompt to login
        return render(request, 'cart/checkout.html', {
            'login': True
        })
