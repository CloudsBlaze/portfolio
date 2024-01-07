from django.db import models
from image.models import Images
from autoslug import AutoSlugField

# Create your models here.


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    service_category_slug = AutoSlugField(
        populate_from="name", editable=True, always_update=True, null=True, blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    service_category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name="service_category"
    )
    service_slug = AutoSlugField(
        populate_from="name", editable=True, always_update=True, null=True, blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServiceImage(Images):
    service_images = models.ForeignKey(
        Service, related_name="service_images", on_delete=models.CASCADE
    )
