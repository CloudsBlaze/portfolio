from django.db import models
from image.models import Images




# Create your models here.

class Event(models.Model):
    STATUS_TYPE_CHOICES = (
        ("1", "Scheduled"),
        ("2", "Postponed"),
        ("3", "Cancelled"),
        ("4", "MovedOnline"),
        ("5", "Rescheduled"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,default="")
    start_date = models.DateTimeField(default=None,null=True)
    end_date = models.DateTimeField(default=None, null=True)
    status_type =  models.CharField(
        max_length=20,
        choices=STATUS_TYPE_CHOICES,
        default="1"
    )
    organizer = models.CharField(max_length=255,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Participant(models.Model):
    name =  models.CharField(max_length=100,default=None, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}-{self.event.title}"
        # return f"{self.user.username} - {self.event.title}"



class EventImage(Images):
    event_images = models.ForeignKey(
        Event, related_name="event_images", on_delete=models.CASCADE
    )