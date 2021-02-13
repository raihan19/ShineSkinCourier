from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Order_info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    delivery_address = models.TextField()
    contact_no = models.CharField(max_length=11)
    delivery_instruction = models.TextField()
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
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
    service_charge = models.IntegerField(default=55)
    delivery_area = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})
