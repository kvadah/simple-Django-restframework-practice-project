from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .seializers import RegisterSerializer, ProductSerializer, OrderSrializer, OrderItemsSrializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from .models import Product, Order, OrderItems


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User registered successfully",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all().order_by('created_at')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def my_orders(request):
    customer = request.user.customer
    orders = Order.objects.get(customer=customer)
    serializer = OrderSrializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def order_detail(request,order_id):
    order=Order.objects.get(id=order_id)
    serializer = OrderSrializer(order)
    return Response(serializer.data)

@api_view(['POST'])
def create_order(request):
    customer = request.user.customer
    items = request.data.get('items')   

    order = Order.objects.create(
        customer=customer,
        total_price=0
    )

    total = 0
    for item in items:
        product = Product.objects.get(id=item['product_id'])
        price = product.price

        OrderItems.objects.create(
            order=order,
            product=product,
            price=price,
        )

        total += price 

    order.total_price = total
    order.save()

    return Response({"message": "Order placed", "order_id": order.id})
