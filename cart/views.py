from django.shortcuts import get_object_or_404, render, redirect
from cart.forms import ConfirmBookingForm
from django.http import HttpResponseRedirect
# from django.contrib import messages
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


def delete_from_cart(request, print_id, print_size):
    cart = request.session.get('cart', {})
    print_option = get_object_or_404(PrintOption, size=print_size)
    print_size_id = print_option.id

    print_key = f"{print_id}{print_size_id}"

    if print_key in list(cart.keys()):
        del cart[print_key]

    request.session['cart'] = cart

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def plus_print_to_cart(request, print_id, print_size):
    cart = request.session.get('cart', {})
    print_option = get_object_or_404(PrintOption, size=print_size)
    print_size_id = print_option.id

    print_key = f"{print_id}{print_size_id}"

    if print_key in list(cart.keys()):
        cart[print_key]['quantity'] += 1

    request.session['cart'] = cart

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def minus_print_from_cart(request, print_id, print_size):
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
    shipping_information_form = ConfirmBookingForm()

    return render(request, 'cart/checkout.html', {
        'is_authenticated': request.user.is_authenticated,
        'shipping_information': shipping_information_form,
        'stripe_public_key': 'pk_test_51N9oqfE5lPSi6ejG4EggglOyiLhas9uGiBQ3av0m91jRVvfCUhgvH2uG8TVs7dG6H0OxwA7SdUN59JQaqM4Ob0qs00bTUi0Ne5',
        'client_secret': 'test client secret',
    })
