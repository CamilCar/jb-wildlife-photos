from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.conf import settings

from cart.forms import ConfirmBookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from webshop.models import PrintOption
from cart.contexts import cart_content

import stripe
# Create your views here.


def add_to_cart(request, print_id):
    """
    Adds a product to cart
    """
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    print_option = get_object_or_404(PrintOption, size=size)
    print_size_id = print_option.id

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # Creates a unique key by combining the
    # print id and the print option id
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


def delete_from_cart(request, print_id, print_size):
    """
    Delete a item from cart
    """
    cart = request.session.get('cart', {})
    print_option = get_object_or_404(PrintOption, size=print_size)
    print_size_id = print_option.id

    print_key = f"{print_id}{print_size_id}"

    if print_key in list(cart.keys()):
        del cart[print_key]

    request.session['cart'] = cart

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def plus_print_to_cart(request, print_id, print_size):
    """
    Adds 1 to a already existing product,
    can not add above 10
    """
    cart = request.session.get('cart', {})
    print_option = get_object_or_404(PrintOption, size=print_size)
    print_size_id = print_option.id

    print_key = f"{print_id}{print_size_id}"

    if print_key in list(cart.keys()):
        if cart[print_key]['quantity'] < 10:
            cart[print_key]['quantity'] += 1

    request.session['cart'] = cart

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def minus_print_from_cart(request, print_id, print_size):
    """
    Removes 1 from cart, deletes from cart if
    it's the last one
    """
    cart = request.session.get('cart', {})
    print_option = get_object_or_404(PrintOption, size=print_size)
    print_size_id = print_option.id

    print_key = f"{print_id}{print_size_id}"

    if print_key in list(cart.keys()):
        if cart[print_key]['quantity'] <= 1:
            del cart[print_key]
        else:
            cart[print_key]['quantity'] -= 1

    request.session['cart'] = cart

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def checkout(request):
    """
    Goes from the cart to checkout.
    Setup stripe payment intent
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('webshop'))

    shipping_information_form = ConfirmBookingForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_cart = cart_content(request)
    total = current_cart['total_sum']
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    return render(request, 'cart/checkout.html', {
        'is_authenticated': request.user.is_authenticated,
        'shipping_information': shipping_information_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    })
