from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class player(models.Model):
	name = models.CharField(max_length=200,null=True)
	number = PhoneNumberField(null=True,blank=True,unique=True)
	description = models.TextField(null=True,blank=True)
	email = models.EmailField(unique=True)
	batchnumber = models.IntegerField()

	
