from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image1 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
