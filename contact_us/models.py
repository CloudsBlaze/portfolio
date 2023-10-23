from django.db import models

# Create your models here.
class Contactus(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
