from django.db import models

class EventAtendee(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    runner = models.ForeignKey("Runner", on_delete=models.CASCADE)