# Generated by Django 4.1.5 on 2023-02-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_alter_cart_options_alter_stock_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_ind_code',
            field=models.CharField(default=0, max_length=16, verbose_name='산업코드'),
            preserve_default=False,
        ),
    ]
