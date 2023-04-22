from django.urls import path
from . import views

urlpatterns = [
    path('', views.webshop, name="webshop"),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
