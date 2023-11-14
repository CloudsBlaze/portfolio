from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


