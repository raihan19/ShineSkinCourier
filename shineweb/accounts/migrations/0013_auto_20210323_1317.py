# Generated by Django 3.1.6 on 2021-03-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_order_received_from_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(blank=True, default='To be assigned', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_instruction',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
