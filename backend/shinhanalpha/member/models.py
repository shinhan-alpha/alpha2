from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    cust_name = models.CharField(max_length=8, verbose_name='성명', null=True)
    acct_no = models.IntegerField(unique=True, verbose_name='계좌번호', null=True)
    acct_pw = models.CharField(max_length=4, default='0000', verbose_name='계좌 비밀번호', null=True)
    status = models.CharField(max_length=16, default='일반',
        choices=(
            ('일반', '일반'),
            ('탈퇴', '탈퇴'),
            ('휴면', '휴면'),
        )
    )

    class Meta:
        db_table = 'member'
        verbose_name = '회원'
        verbose_name_plural = '회원'
    