from django.urls import path
from . import views

urlpatterns = [
    path('', views.webshop, name="webshop"),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
]
