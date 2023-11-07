from rest_framework import serializers
from django.contrib.auth.models import User
#from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product, Order, OrderItem, ShippingAddress

class ProductSerializer(serializers.ModelSerializer):
   # reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

