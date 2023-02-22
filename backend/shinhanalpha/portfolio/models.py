from django.db import models

# Create your models here.
class Portfolio(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='회원')
    stock = models.IntegerField(verbose_name='주식 비율')
    bond = models.IntegerField(verbose_name='채권 비율')
    real_asset = models.IntegerField(verbose_name='실물자산 비율')
    crypto = models.IntegerField(verbose_name='가상화폐 비율')

    class Meta:
        db_table = 'portfolio'
        verbose_name = '총자산 포트폴리오'
        verbose_name_plural = '총자산 포트폴리오'

class Dividend(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='회원')
    january = models.IntegerField(verbose_name='1월')
    february = models.IntegerField(verbose_name='2월')
    march = models.IntegerField(verbose_name='3월')
    april = models.IntegerField(verbose_name='4월')
    may = models.IntegerField(verbose_name='5월')
    june = models.IntegerField(verbose_name='6월')
    july = models.IntegerField(verbose_name='7월')
    august = models.IntegerField(verbose_name='8월')
    september = models.IntegerField(verbose_name='9월')
    october = models.IntegerField(verbose_name='10월')
    november = models.IntegerField(verbose_name='11월')
    december = models.IntegerField(verbose_name='12월')

    class Meta:
        db_table = 'dividend'
        verbose_name = '배당금 포트폴리오'
        verbose_name_plural = '배당금 포트폴리오'
