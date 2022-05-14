from django.db import models
from home.models import Properties   

class Cleaning(models.Model): 
    properties=models.ForeignKey(Properties, on_delete=models.CASCADE)
    linnen = models.CharField(max_length=256)
    access = models.CharField(max_length=256)
    points_of_attention=models.CharField(max_length=256)
	