# Generated by Django 3.1.6 on 2021-03-01 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0008_auto_20210224_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_info_price',
            name='delivery_option',
        ),
        migrations.DeleteModel(
            name='order_info',
        ),
        migrations.DeleteModel(
            name='Order_info_delivery',
        ),
        migrations.DeleteModel(
            name='Order_info_price',
        ),
    ]