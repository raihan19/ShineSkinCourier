from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Order_info_delivery(models.Model):
    d_opt = [
        ('InDh', 'Inside Dhaka (ID: 241)'),
        ('DhSub', 'Dhaka Sub (ID: 242)'),
        ('OutDh', 'Outside Dhaka HD (ID: 243)'),
    ]
    delivery_option = models.CharField(
        max_length=30,
        choices=d_opt,
        default='Please select',
    )

class Order_info_price(models.Model):
    delivery_option = models.ForeignKey(Order_info_delivery, on_delete=models.CASCADE)
    service_charge = models.IntegerField(default=55)

class Order_info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    delivery_address = models.TextField()
    contact_no = models.CharField(max_length=11)
    delivery_instruction = models.TextField()
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_option = models.ForeignKey(Order_info_delivery, on_delete=models.SET_NULL, null=True)
    service_charge = models.ForeignKey(Order_info_price, on_delete=models.SET_NULL, null=True)
    delivery_area = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})
