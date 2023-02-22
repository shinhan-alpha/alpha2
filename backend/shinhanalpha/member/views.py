from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from .serializers import MemberSerializer

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    # 로그인된 사용자만 들어올수있음
    def put(self, request, *arg, **kwargs):

        password = request.data.get('password')
        password_change = request.data.get('password_change')
        password_change_check = request.data.get('password_change_check')

        if password_change != password_change_check:
            return Response({
                'detail': 'Wrong new passwords'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        member = request.user
        if not check_password(password, member.password):
            return Response({
                'detail': 'Wrong password'
            }, status=status.HTTP_400_BAD_REQUEST)

        member.password = make_password(password_change)
        member.save()
        
        return Response(status=status.HTTP_200_OK)
