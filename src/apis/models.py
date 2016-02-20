from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Api(models.Model):
    """this model store the definition for the Apis"""
    name = models.CharField(max_length=50)
    uri = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class ChartVisualization(models.Model):
    """this model store the information for each ChartVisualization"""
    name = models.CharField(max_length=10)
    status = models.BooleanField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def natural_key(self):
        return self.name
    def __str__(self):
        return self.name


class ChartType (models.Model):
    """this model store the information for each ChartType"""
    name = models.CharField(max_length=10)
    status = models.BooleanField(default=1)
    chartVisualization = models.ForeignKey(ChartVisualization, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name

class Chart(models.Model):
    """this is abstract model for Chart"""
    CHART_SIZES = (
        ('1', '1x'),
        ('2', '2x'),
        ('3', '3x'),
    )
    name = models.CharField(max_length=50)
    chartType = models.ForeignKey(ChartType, on_delete=models.CASCADE)
    apis = models.ForeignKey(Api, on_delete=models.CASCADE)
    size = models.CharField(help_text="size of your chart", max_length=2,choices=CHART_SIZES)
    dataSet = models.CharField(max_length=20)
    attribute = models.CharField(max_length=20)
    dimensions = models.CharField(max_length=100)
    options =  models.CharField(max_length=100)
    status = models.BooleanField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #   # return self.name
    #   return u"%s" % self.id
    def __str__(self):
        return "%s" % self.name
        
class DashBoard(models.Model):
    """this model store the information for each DashBoard that you define"""
    name = models.CharField(max_length=50)
    default =  models.BooleanField()
    status = models.BooleanField(default=1)
    charts = models.ManyToManyField(Chart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
    def __str__(self):
        return "%s" % self.name

# class SignUp(models.Model):
#   """this model store the information for SignUp"""
#   email = models.EmailField()
#   full_name = models.CharField(max_length=120,blank=False,null=True)
#   timestamp = models.DateTimeField(auto_now_add=True)
#   updated = models.DateTimeField(auto_now=True)
    
#   def  __str__(self):
#       return self.email