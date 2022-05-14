from django.db import models
from home.models.cleaners import Cleaners

class Cleaners(models.Model):
    name=models.CharField(max_length=200)	
    email=models.EmailField(max_length=254)	
    password=models.CharField(max_length=200)	
    phone=models.BigIntegerField()
    location=models.TextField()	
    details=models.TextField()
    role=models.TextField()	

class CleanersReport(models.Model):
    cleaners=models.ForeignKey(Cleaners,on_delete=models.CASCADE)	
    date=models.DateField()	
    task_status=models.CharField(max_length=255)	
    task_content=models.CharField(max_length=255)	
    location=models.CharField(max_length=255)	
    propertyname=models.CharField(max_length=255)	
    address	=models.TextField()
    starting_hours=models.CharField()	
    ending_hours=models.CharField()	
    time_period=models.CharField()	
    working_hours=models.CharField()
    
class CleansersImage(models.Model):
    cleaners=models.ForeignKey(Cleaners,on_delete=models.CASCADE)
    image =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    uploded_at=models.DateTimeField(auto_now=False, auto_now_add=False)