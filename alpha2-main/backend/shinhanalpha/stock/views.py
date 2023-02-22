from django.shortcuts import render
from rest_framework import mixins, generics

from .serializers import StockSerializer, CartSerializer, CartCreateSerializer, CartDeleteSerializer, BalanceSerializer
from .models import Stock, Cart, Balance
# Create your views here.

class StockListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = StockSerializer

    def get_queryset(self):
        stocks = Stock.objects.all()
        return stocks

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

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
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CartSerializer

    def get_queryset(self):
        stock_id = self.kwargs.get('stock_id')
        if stock_id:
            return Cart.objects.filter(stock_id=stock_id) \
                .select_related('user', 'stock') \
                .stock_by('-id')
        return Cart.objects.none()

    def get(self,request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class CartCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):  
    serializer_class = CartCreateSerializer

    def get_queryset(self):
        stock_id = self.kwargs.get('stock_id')
        if stock_id:
            return Cart.objects.filter(stock_id=stock_id) \
                .select_related('user', 'stock') \
                .filter()
        return Cart.objects.none()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    

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