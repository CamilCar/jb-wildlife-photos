from django.urls import path
from . import views

urlpatterns = [
    path('create_order/<payment_intent_id>/', views.create_order,
         name='create_order'),
]
