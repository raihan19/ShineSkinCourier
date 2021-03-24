# Generated by Django 3.1.6 on 2021-03-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20210324_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_received_or_sent',
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_received',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(blank=True, default='To be assigned', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='due',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='received_from_customer',
            field=models.IntegerField(default=0),
        ),
    ]
