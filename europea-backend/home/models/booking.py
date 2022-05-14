from django.db import models
from home.models import Properties 
class Booking(models.Model):    
    properties=models.ForeignKey(Properties, on_delete=models.CASCADE)
    title =	models.CharField(max_length=200)	    
    start_date=models.DateField() 
    end_date=models.DateField()
    
