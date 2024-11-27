from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField
from .models import *

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'password']
    
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user

class CustomerSerializer(ModelSerializer):
  class Meta:
    model = Customer
    fields = ['profileimg', 'name', 'phone', 'email', 'address']

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = ['id', 'name', 'prodimg', 'rate', 'description']

class OrderSerializer(ModelSerializer):
  customer = CustomerSerializer()

  class Meta:
    model = Order
    fields = ['id', 'slug', 'total', 'status', 'note', 'date_created', 'customer']

class OrderItemSerializer(ModelSerializer):
  product = ProductSerializer()

  class Meta:
    model = OrderItem
    fields = ['id', 'product', 'quantity', 'price']