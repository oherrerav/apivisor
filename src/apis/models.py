from django.db import models

# Create your models here.
class Api(models.Model):
	"""this model store the definition for the Apis"""
	name = models.CharField(max_length=50)
	uri = models.CharField(max_length=500)

	def __str__(self):
		return self.name


class SignUp(models.Model):
	"""this model store the information for SignUp"""
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=False,null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def  __str__(self):
		return self.email