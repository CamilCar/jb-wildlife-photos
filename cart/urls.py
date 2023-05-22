from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/<print_id>/', views.add_to_cart, name="add_to_cart"),
    path('delete/<print_id>/<print_size>', views.delete_from_cart, name="delete_from_cart"),
    path('plus/<print_id>/<print_size>', views.plus_print_to_cart, name="plus_print_to_cart"),
    path('minus/<print_id>/<print_size>', views.minus_print_from_cart, name="minus_print_from_cart"),
    path('checkout/', views.checkout, name='checkout'),
]
