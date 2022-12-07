from django.db import models
from django.contrib.auth.models import User

class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    zipcode = models.IntegerField()

    @property
    def runner_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    