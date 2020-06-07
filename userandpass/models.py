from django.db import models

# Create your models here.

class Userandpass(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    security_key = models.CharField(max_length=250)
    