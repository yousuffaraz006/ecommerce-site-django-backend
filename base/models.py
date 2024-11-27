from django.contrib.auth.models import User
from django.db import models
import random

class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  profileimg = models.ImageField(upload_to='base/images/', default='base/images/user.png', blank=True, null=True)
  name = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  address = models.TextField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return str(self.user)

class Product(models.Model):
  name = models.CharField(max_length=200, null=True)
  prodimg = models.ImageField(upload_to='base/images/', blank=True, null=True)
  rate = models.FloatField(null=True)
  description = models.CharField(max_length=200, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return str(self.name)

class Order(models.Model):
  slug = models.SlugField(unique=True, null=True, blank=True)
  customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
  status = models.CharField(max_length=200, null=True, default='Pending')
  note = models.CharField(max_length=1000, null=True, blank=True, default='Your order has been placed successfully!')
  total = models.CharField(max_length=20, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return str(self.slug)

  def save(self, *args, **kwargs):
    if not self.slug:
      # Generate slug
      slug_base = random.randint(100, 999)
      slug_id = random.randint(10000000, 99999999)
      self.slug = f"#{slug_base}-{slug_id}"
    super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(null=True)
  price = models.CharField(max_length=20, null=True, blank=True)

  def __str__(self):
    return self.order.slug