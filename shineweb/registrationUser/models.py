from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

# Create your models here.
class regProfile(models.Model):
    PAYMENT_CHOICE = (
        ('Bank', 'Bank'),
        ('bKash', 'bKash'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    your_name = models.CharField(max_length=100, default='')
    contact_no = models.CharField(max_length=11)
    company_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=200, null=True, choices=PAYMENT_CHOICE)
    way_of_payment = models.CharField(max_length=50, default='')
    company_address = models.TextField()

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
