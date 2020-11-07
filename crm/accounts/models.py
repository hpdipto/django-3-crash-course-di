from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

	def __str__(self):
		return self.name

	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


class Tag(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200, null=True)



class Product(models.Model):

	def __str__(self):
		return self.name

	CATEGORY = (('Indoor', 'Indoor'),
							('Outdoor', 'Outdoor'))

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)



class Order(models.Model):

	def __str__(self):
		return self.product.name

	STATUS = (('Pending', 'Pending'),
						('Out for delivery', 'Out for delivery'),
						('Delivered', 'Delivered'))
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)