from django.urls import path
from .views import *

urlpatterns = [
  path('profile/', Profile, name='profile'),
  path('products/', Products, name='products'),
  path('product/<str:pk>/', ProductDetails, name='product'),
  path('orders/', Orders, name='orders'),
  path('order/<str:pk>/', OrderDetails, name='order'),
  path('orderspage/', OrdersPage, name='orderspage'),
  path('orderpage/<str:pk>/', OrderDetailsPage, name='orderpage'),
]