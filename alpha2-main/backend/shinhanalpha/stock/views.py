from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import StockSerializer, CartSerializer, CartCreateSerializer, CartDeleteSerializer, BalanceSerializer
from .models import Stock, Cart, Balance
# Create your views here.

class StockListView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = StockSerializer

    def get_queryset(self):
        stocks = Stock.objects.all()
        return stocks

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class StockDetailView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = StockSerializer

    def get_queryset(self):
        stocks = Stock.objects.all()
        return stocks

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class CartListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):  
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CartCreateSerializer
        return CartSerializer

    def get_permission_class(self):
        if self.request.method == 'POST':
            return [IsAuthenticated]
        return 

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Cart.objects.filter(member_id = pk).order_by('-id')
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CartDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    serializer_class = CartDeleteSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Cart.objects.filter(pk=pk) \
                .select_related('user', 'stock') \

        return Cart.objects.none()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
    
class BalanceListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = BalanceSerializer

    def get_queryset(self):
        balance = Balance.objects.all()
        return balance

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)