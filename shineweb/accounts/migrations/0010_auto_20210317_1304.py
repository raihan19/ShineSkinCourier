# Generated by Django 3.1.6 on 2021-03-17 13:04

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210308_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(default=accounts.models.random_choice, editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]