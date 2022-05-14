from django.db import models
from home.models.owners import Owners


class Properties(models.Model):
    owners = models.ForeignKey(Owners, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
    img = models.CharField(max_length=256, null=True)
    min_stay = models.CharField(max_length=256, null=True)
    quota = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=256, null=True)
    pr_no = models.CharField(max_length=256, null=True)
    max_nights = models.CharField(max_length=256, null=True)
    property_status = models.CharField(max_length=256, null=True)
    last_update = models.CharField(max_length=256, null=True)
