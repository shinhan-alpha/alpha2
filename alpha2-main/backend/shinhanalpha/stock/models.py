from django.db import models

# Create your models here.

class Stock(models.Model):
    stock_code = models.CharField(max_length=16, verbose_name='종목코드')
    stock_name = models.CharField(max_length=16, verbose_name='종목명')
    stock_cp = models.CharField(max_length=32, verbose_name='현재가')
    stock_pg = models.CharField(max_length=16, verbose_name='전일대비금액')
    stock_pr = models.CharField(max_length=16, verbose_name='전일대비등락률')

    class Meta:
        db_table='stock'
        verbose_name = '주식'
        verbose_name_plural = '주식'


class Cart(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='회원')
    stock_name = models.CharField(max_length=32, verbose_name='종목명')
    stock_code = models.CharField(max_length=16, verbose_name='종목코드')
    buy_price = models.CharField(max_length=16, verbose_name='매수가')
    buy_quantity = models.IntegerField(verbose_name='매수수량')

    class Meta:
        db_table = 'stock_cart'
        verbose_name = '장바구니'
        verbose_name_plural = '장바구니'


class Balance(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='회원')
    cart = models.ForeignKey('stock.Cart', on_delete=models.CASCADE, verbose_name='장바구니')
    deposit = models.IntegerField(verbose_name='예수금')

    class Meta:
        db_table = 'balance'
        verbose_name = '주식잔고'
        verbose_name_plural = '주식잔고'