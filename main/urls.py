from django.urls import path
from .views import RegisterView, product_list, create_order, my_orders, order_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns=[
  path('auth/register/', RegisterView.as_view(),name='register') , 
  path('auth/login/', TokenObtainPairView.as_view(),name='login'),
  path('auth/refresh/', TokenRefreshView.as_view(),name='refresh'),
  path('products/',product_list,name='products')
  path("orders/create/", create_order),
  path("orders/", my_orders),
  path("orders/<int:order_id>/", order_detail),

]