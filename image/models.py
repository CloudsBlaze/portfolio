from django.db import models
# from django.contrib.auth.models import User
from events.models import Event
# from django.conf import settings

# Create your models here.

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        # return self.event
        return f"Image for {self.event.name}"