from django import models
from django.contrib.auth.models import User

class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mileage = models.Integer(max_length=5)
    zipcode = models.Integer(max_length=5)
    