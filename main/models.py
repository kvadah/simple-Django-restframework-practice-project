from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer')
    usernname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.usernname


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    image_link = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='ordered_by')
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.total_price)


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.quantity} {self.product.product_name}"
