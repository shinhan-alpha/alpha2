from rest_framework import serializers
from .models import Stock, Cart, Balance

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stock
        fields='__all__'


class CartSerializer(serializers.ModelSerializer):
    member_username = serializers.SerializerMethodField()

    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model = Cart
        fields = '__all__'


class CartCreateSerializer(serializers.ModelSerializer):
    # 로그인 된 정보(CurrentuserDefault)를 자동으로 불러옴
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required=False
    )

    def validate_user(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError("user is required")
        return value
    
    class Meta:
        model = Cart
        fields = '__all__'

class CartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Balance
        fields='__all__'