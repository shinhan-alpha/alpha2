from django.contrib.auth.hashers import check_password
from .models import Member

class MemberAuth:

    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if not username or not password:
            if request.user.is_authenticated:
                return request.user
            return None

        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None
        
        if member.status == '일반':
            # if 일회용비밀번호?
            if check_password(password, member.password):
                return member
        return None
    
    def get_user(self, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None
        return member