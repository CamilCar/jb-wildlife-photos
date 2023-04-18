from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('pricing/', views.pricing, name='pricing'),
]
