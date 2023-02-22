from rest_framework import serializers
from .models import Stock, Cart, Balance

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stock
        fields='__all__'


class CartSerializer(serializers.ModelSerializer):
    stock_stock_code = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )
    def get_stock_stock_code(self, obj):
        return obj.stock.stock_code

    def get_member_username(self, obj):
        return obj.user.username

    class Meta:
        model = Cart
        fields = '__all__'


class CartCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )

    def validate_user(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required')
        return value

    class Meta:
        model = Cart
        fields = '__all__'

class CartDeleteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    def validate_user(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required')
        return value

    class Meta:
        model = Cart
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Balance
        fields='__all__'