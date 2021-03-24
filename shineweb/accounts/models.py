from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import string
import random
import datetime
# Create your models here.

def random_choice():
	date_object = ''.join(str(datetime.date.today()).split('-'))
	alphabet = string.ascii_lowercase + string.digits
	return date_object + '-' + ''.join(random.choices(alphabet, k=8))

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


# class Order_delivery(models.Model):
# 	delivery_option = models.CharField(max_length=20)
#
# 	def __str__(self):
# 		return self.delivery_option


# class Order_price(models.Model):
# 	delivery_option = models.ForeignKey(Order_delivery, on_delete=models.CASCADE)
# 	service_charge = models.CharField(max_length=5)
#
# 	def __str__(self):
# 		return str(self.service_charge)

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


class All_area(models.Model):
	delivery_area = models.CharField(max_length=20)

	def __str__(self):
		return self.delivery_area


class Product_category(models.Model):
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.category


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Returned', 'Returned'),
			('Delivered', 'Delivered'),
			)

	merchant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	id = models.CharField(primary_key=True, max_length=20, default=random_choice, editable=False)
	customer_name = models.CharField(max_length=200, null=True, blank=True)
	customer_phone = models.CharField(max_length=200, null=True, blank=True)
	customer_email = models.CharField(max_length=200, null=True, blank=True)
	product_name = models.CharField(max_length=200, null=True, blank=True)
	product_price = models.FloatField(null=True, blank=True)
	product_category = models.ForeignKey(Product_category, on_delete=models.SET_NULL, null=True, blank=True)
	product_description = models.TextField(default='', blank=True)
	# delivery_option = models.ForeignKey(Order_delivery, on_delete=models.SET_NULL, null=True)
	# service_charge = models.ForeignKey(Order_price, on_delete=models.SET_NULL, null=True)
	product_weight = models.CharField(max_length=10, default='', blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)
	note = models.CharField(max_length=1000, null=True, blank=True)
	delivery_address = models.TextField(default='', blank=True)
	delivery_instruction = models.TextField(default='', blank=True)
	delivery_area = models.ForeignKey(All_area, on_delete=models.SET_NULL, null=True, blank=True)
	received_from_customer = models.IntegerField(default=0, blank=True)
	amount = models.IntegerField(default=0, blank=True)
	total_received_or_sent = models.IntegerField(default=0, blank=True)
	due = models.IntegerField(default=0, blank=True)

	def save(self, *args, **kwargs):
		self.due = self.received_from_customer - self.amount - self.total_received_or_sent
		return super(Order, self).save()

	def __str__(self):
		return str(self.merchant) + ' ' + str(self.id)

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})

	@property
	def orders(self):
		try:
			order_count = self.order_set.all().count()
			return str(order_count)
		except:
			pass


