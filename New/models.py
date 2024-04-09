from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey('Publisher', on_delete=models.CASCADE)

class Location(models.Model):
    name = models.CharField(max_length=50)