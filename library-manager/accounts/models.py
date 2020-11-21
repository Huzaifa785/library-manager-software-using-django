from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
	user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="user.jpg", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return str(self.name)

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.name)

class Book(models.Model):
	CATEGORY = (
			('Horror Stories', 'Horror Stories'),
			('Fairy Tales', 'Fairy Tales'),
			('Mysterious', 'Mysterious'),
			('Comedy', 'Comedy'),
			('Tragedy', 'Tragedy'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return str(self.name)

class Order(models.Model):
	STATUS = (
			('Returned', 'Returned'),
			('Have To Return', 'Have To Return'),
			)

	customer = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL) 
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.product.name)