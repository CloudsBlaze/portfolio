from django.db import models
# from django.contrib.auth.models import User


# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to="image_files/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.event
        return f"Image for {self.id}"