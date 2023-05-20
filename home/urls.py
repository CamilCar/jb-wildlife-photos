from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('policy/', views.policy, name='policy'),
    path('pricing/', views.pricing, name='pricing'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('update_status/<order_id>/<new_status>', views.update_status,
         name="update_status")
]
