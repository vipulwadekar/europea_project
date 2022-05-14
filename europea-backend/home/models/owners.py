from django.db import models


class Owners(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=150, null=True)
    password = models.CharField(max_length=50, null=True)
