from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class regProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    your_name = models.CharField(max_length=100, default='')
    contact_no = models.CharField(max_length=11)
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()

    # def __str__(self):
    #     return self.user.name
