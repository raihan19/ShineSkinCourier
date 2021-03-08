# Generated by Django 3.1.6 on 2021-03-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210302_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='merchant_payment_method',
            field=models.CharField(choices=[('Bank', 'Bank'), ('bKash', 'bKash')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='way_of_payment',
            field=models.CharField(default='', max_length=50),
        ),
    ]