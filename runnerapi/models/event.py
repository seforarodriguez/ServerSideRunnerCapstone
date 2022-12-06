from django.db import models

class Event(models.Model):
    park = models.ForeignKey("Park", on_delete=CASCADE)
    date = models.DateField()
    time = models.TimeField()
    pace_of_run = models.IntegerField()
    miles_to_run = models.IntegerField()
    organizer = models.ForeignKey("Runner", on_delete=models.CASCADE)
