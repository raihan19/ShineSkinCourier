# Generated by Django 3.1.6 on 2021-02-12 11:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ordersite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='delivery_status',
            new_name='order_info',
        ),
    ]
