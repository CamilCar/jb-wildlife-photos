from django.shortcuts import redirect, render

from orders.models import Order

# Create your views here.


def create_order(request):
    if request.user.is_authenticated:
        print("creating order")
        cart = request.session.get('cart', {})
        print(cart)
    else:
        print("you must create an account first")
        return redirect('/home')
