from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Event(models.Model):
    STATUS_TYPE_CHOICES = (
        ("Postbond", "Postbond"),
        ("Cancel", "Cancel"),
        ("Continue", "Continue"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,default="")
    start_date = models.DateTimeField(default=None,null=True)
    end_date = models.DateTimeField(default=None, null=True)
    status_type = models.CharField(
        max_length=20,
        choices=STATUS_TYPE_CHOICES,
        default="Postbond"
    )
    organizer = models.CharField(max_length=255,blank=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"