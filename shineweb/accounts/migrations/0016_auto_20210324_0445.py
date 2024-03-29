# Generated by Django 3.1.6 on 2021-03-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210324_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='due',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='received_from_customer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_received_or_sent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
