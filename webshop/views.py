import json
from django.shortcuts import get_object_or_404, redirect, render

from .models import Cart, CartItem, Print, Category

# Create your views here.


def webshop(request):
    """ Returns webshop page, including filter """
    prints = None
    categories = Category.objects.all()

    if 'category' in request.GET:
        categoryToFind = request.GET['category']
        prints = Print.objects.filter(category=categoryToFind)
    else:
        prints = Print.objects.all()

    return render(request, 'webshop/gallery.html', {
        'categories': categories,
        'prints': prints
    })


def product_detail(request, pk):
    product = get_object_or_404(Print, pk=pk)

    prices = {
        'a4': 30,
        'a3': 40,
        'a3+': 50,
    }

    return render(request, 'webshop/product_detail.html', {
        'print': product,
        'prices': json.dumps(prices)
    })


def add_to_cart(request):
    print_id = request.POST['print_id']

    product = get_object_or_404(Print, pk=print_id)

    cart_for_user, cart_item = None, None
    price, size = request.POST['price'], request.POST['size']

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            print=product,
            price=price,
            size=size
        )

        cart_for_user = Cart.objects.filter(user=request.user, completed=False)
    else:
        cart_item, created = CartItem.objects.get_or_create(
            print=product,
            price=price,
            size=size
        )
        cart_for_user = Cart.objects.filter(user=None, completed=False, session_key=request.session.session_key)

    # add or update cart
    add_or_update_to_cart(cart_for_user, cart_item, request)
    return redirect("product_detail/" + print_id)


def add_or_update_to_cart(cart_for_user, cart_item: CartItem, request):
    print_id = request.POST['print_id']
    if cart_for_user.exists():
        order = cart_for_user[0]
        if cart_item.print == print_id:
            cart_item.amount += 1
            cart_item.save()
        else:
            order.prints.add(cart_item)
    else:
        order = None
        if request.user.is_authenticated:
            order = Cart.objects.create(
                user=request.user
            )
        else:
            order = Cart.objects.create(
                user=None, session_key=request.session.session_key
            )
        order.prints.add(cart_item)
