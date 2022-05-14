from django.db import models

class CommentReport(models.Model):
	property_name = models.CharField(max_length=255)	
	date_time=models.DateTimeField(auto_now=False, auto_now_add=False)	
	cleaner_name=models.CharField(max_length=200)	
	location=models.TextField()		
	address=models.TextField()		
	comment=models.TextField()	