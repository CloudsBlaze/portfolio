from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Event(models.Model):
    STATUS_TYPE_CHOICES = (
        ("1", "Postponed"),
        ("2", "Cancel"),
        ("3", "Continue"),
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
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Participant(models.Model):
    name =  models.CharField(max_length=100,default=None, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}-{self.event.title}"
        # return f"{self.user.username} - {self.event.title}"