from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product,Customer,Order,OrderItems

class RegisterSerializer(serializers.ModelSerializer):
    password =serializers.CharField(write_only =True)

    class Meta:
        model = User
        fields = ['username', 'email','password']
    def create (self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Customer.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )
        return user
    


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"


class OrderSrializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields= "__all__"


class OrderItemsSrializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields= "__all__"