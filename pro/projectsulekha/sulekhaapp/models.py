from __future__ import unicode_literals
from django.db import models


class Users(models.Model):
	first_name=models.CharField(max_length=120)
	last_name=models.CharField(max_length=120)
	email=models.EmailField()
	password=models.CharField(max_length=60)

	def __unicode__(self):
		return self.email

class Posts(models.Model):
	house_type = models.CharField(max_length = 120)
	rooms = models.IntegerField(default = 0)
	location = models.CharField(max_length = 100)
	address = models.CharField(max_length = 150)
	city = models.CharField( max_length = 150)
	state = models.CharField( max_length = 20)
	zipcode = models.IntegerField(default = 0)
	images = models.FileField( null = True)
	details = models.CharField( max_length = 250)

	def __unicode__(self):
		return self.house_type
