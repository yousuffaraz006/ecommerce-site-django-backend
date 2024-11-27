from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .serializers import *
from .models import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['fullname'] = user.first_name + " " + user.last_name
    token['group'] = user.groups.all()[0].name

    return token
      
class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def Profile(request):
  customer = Customer.objects.get(user=request.user)
  if request.method == 'GET':
    serializer = CustomerSerializer(customer)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    print(request.data)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Products(request):
  if request.method == 'GET':
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ProductDetails(request, pk):
  product = Product.objects.get(id=pk)
  if request.method == 'GET':
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    print(request.data)
    serializer = ProductSerializer(product, data=request.data)
    print(serializer)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    product.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def OrdersPage(request):
  if request.method == 'GET':
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def OrderDetailsPage(request, pk):
  order = Order.objects.get(id=pk)
  if request.method == 'GET':
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    serializer = OrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Orders(request):
  customer = Customer.objects.get(user=request.user)
  if request.method == 'GET':
    orders = Order.objects.filter(customer=customer).order_by('-date_created')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    data = request.data
    order = Order.objects.create(
      customer=customer,
      total = data.get('total')
    )
    order.save()
    items = data.get('items', [])
    for item_data in items:
      product = Product.objects.get(id=item_data.get('product'))
      quantity = item_data.get('quantity')
      price = item_data.get('price')
      OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def OrderDetails(request, pk):
  order = Order.objects.get(id=pk)
  order_items = OrderItem.objects.filter(order=order)
  serializer = OrderItemSerializer(order_items, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)