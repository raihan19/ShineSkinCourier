from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# class Customer(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#
# 	def __str__(self):
# 		return self.name
#
# 	@property
# 	def orders(self):
# 		order_count = self.order_set.all().count()
# 		return str(order_count)


class Order_delivery(models.Model):
	delivery_option = models.CharField(max_length=20)

	def __str__(self):
		return self.delivery_option


class Order_price(models.Model):
	delivery_option = models.ForeignKey(Order_delivery, on_delete=models.CASCADE)
	service_charge = models.CharField(max_length=5)

	def __str__(self):
		return str(self.service_charge)

#
# class Product(models.Model):
#
# 	CATEGORY = (
# 			('Indoor', 'Indoor'),
# 			('Out Door', 'Out Door'),
# 			)
#
# 	name = models.CharField(max_length=200, null=True)
# 	price = models.FloatField(null=True)
# 	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
# 	description = models.TextField()
# 	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#
# 	def __str__(self):
# 		return self.name



class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	CATEGORY = (
		('Phone', 'Phone'),
		('Accessories', 'Accessories'),
	)

	PAYMENT_CHOICE = (
		('Bank', 'Bank'),
		('bKash', 'bKash'),
	)

	merchant = models.ForeignKey(User, on_delete=models.CASCADE)
	merchant_payment_method = models.CharField(max_length=200, null=True, choices=PAYMENT_CHOICE)
	way_of_payment = models.CharField(max_length=50, default='')
	customer_name = models.CharField(max_length=200, null=True)
	customer_phone = models.CharField(max_length=200, null=True)
	customer_email = models.CharField(max_length=200, null=True)
	product_name = models.CharField(max_length=200, null=True)
	product_price = models.FloatField(null=True)
	product_category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	product_description = models.TextField(default='')
	delivery_option = models.ForeignKey(Order_delivery, on_delete=models.SET_NULL, null=True)
	service_charge = models.ForeignKey(Order_price, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	delivery_address = models.TextField(default='')
	delivery_instruction = models.TextField(default='')
	delivery_area = models.CharField(max_length=30, default='')

	def __str__(self):
		return str(self.customer_name) + ' ' + str(self.product_name)

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})

	@property
	def orders(self):
		try:
			order_count = self.order_set.all().count()
			return str(order_count)
		except:
			pass


