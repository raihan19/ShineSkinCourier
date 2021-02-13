# Generated by Django 3.1.6 on 2021-02-13 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0002_auto_20210212_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_info',
            old_name='address',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='order_info',
            old_name='d_area',
            new_name='delivery_area',
        ),
        migrations.RenameField(
            model_name='order_info',
            old_name='d_instruction',
            new_name='delivery_instruction',
        ),
        migrations.RenameField(
            model_name='order_info',
            old_name='d_opt',
            new_name='delivery_option',
        ),
    ]