from django.db import models

# Create your models here.
class Api(models.Model):
	"""this model store the definition for the Apis"""
	name = models.CharField(max_length=50)
	uri = models.CharField(max_length=500)
	user = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class ChartVisualization(models.Model):
	"""this model store the information for each ChartVisualization"""
	name = models.CharField(max_length=10)
	status = models.BooleanField(default=1)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name


class ChartType (models.Model):
	"""this model store the information for each ChartType"""
	name = models.CharField(max_length=10)
	status = models.BooleanField(default=1)
	chartVisualization = models.ForeignKey(ChartVisualization)
	status = models.BooleanField(default=1)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name

class Chart(models.Model):
	"""this model store the information for each Chart that you define"""
	name = models.CharField(max_length=50)
	chartType = models.ForeignKey(ChartType)
	api = models.ForeignKey(Api)
	status = models.BooleanField(default=1)
	user = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class DashBoard(models.Model):
	"""this model store the information for each DashBoard that you define"""
	name = models.CharField(max_length=50)
	chart = models.ForeignKey(Chart)
	default =  models.BooleanField()
	status = models.BooleanField(default=1)
	user = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


# class SignUp(models.Model):
# 	"""this model store the information for SignUp"""
# 	email = models.EmailField()
# 	full_name = models.CharField(max_length=120,blank=False,null=True)
# 	timestamp = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)
	
# 	def  __str__(self):
# 		return self.email