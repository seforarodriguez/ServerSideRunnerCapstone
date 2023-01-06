from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    park = models.ForeignKey("Park", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    pace_of_run = models.IntegerField()
    miles_to_run = models.IntegerField()
    organizer = models.ForeignKey("Runner", on_delete=models.CASCADE)
    attendees= models.ManyToManyField("Runner", through="EventAttendee", related_name='events_assisting')

    @property
    def going(self):
        return self.__going

    @going.setter
    def going(self, value):
        self.__going = value