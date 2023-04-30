from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from webshop.models import Print, PrintOption


def cart_content(request):

    cart_items = []
    total = 0
    delivery = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for cart_id, cart_details in cart.items():
        print_id = cart_details['id']
        product = get_object_or_404(Print, pk=print_id)

        chosen_size = cart_details['size']
        quantity = cart_details['quantity']

        print_option = get_object_or_404(PrintOption, size=chosen_size)

        total += int(print_option.price) * int(quantity)
        
        product_count += int(quantity)

        cart_items.append({
            'print_id': print_id,
            'quantity': quantity,
            'print': product,
            'size': chosen_size
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_calculator = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_calculator = 0

    total_sum = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_calculator': free_delivery_calculator,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total_sum': total_sum,
    }

    return context
