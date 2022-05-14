import imp
from pyexpat import model
from turtle import title
from django.db import models
from models.cleaners import Cleaners
class Events(models.Model):
    cleaners=models.ForeignKey(Cleaners,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)	
    start_at =models.DateTimeField(auto_now=False, auto_now_add=False)
    end_at =models.DateTimeField(auto_now=False, auto_now_add=False)
