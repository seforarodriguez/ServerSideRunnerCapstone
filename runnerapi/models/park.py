from django.db import models
from django.contrib.auth.models import User

class Park(models.Model):
    name = models.CharField(max_length=300)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    miles_available_to_run = models.IntegerField()
    difficulty = models.IntegerField()