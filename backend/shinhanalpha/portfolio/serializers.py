from rest_framework import serializers
from .models import Portfolio, Dividend

class PortfolioSerializer(serializers.ModelSerializer):
    # 로그인 된 정보(CurrentuserDefault)를 자동으로 불러옴
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required=False
    )
    class Meta:
        model=Portfolio
        fields='__all__'
